# sslcheck main

import os
import re
import shutil
from stat import S_ISDIR
from subprocess import check_output

import click

log_dir = "/var/log/qmail/smtpsd"
cache_dir = "./.cache"

MAX_SESSION_LINES = 100


class Session:
    def __init__(self, addr):
        self.addr = addr
        self.ok = 0
        self.fail = 0
        self.count = 0

    def __str__(self):
        return "%s %d %d %d" % (self.addr, self.count, self.ok, self.fail)

    def dict(self):
        return dict(count=self.count, ok=self.ok, fail=self.fail)

    def bump_count(self):
        self.count += 1
        return self

    def bump_fail(self):
        self.fail += 1
        return self.bump_count()

    def bump_ok(self):
        self.ok += 1
        return self.bump_count()


class Sessions:
    def __init__(self):
        self.sessions = {}
        self.total = Session("total")

    def total(self):
        return self.total

    def keys(self):
        return self.sessions.keys()

    def values(self):
        return self.sessions.values()

    def bump(self, label, ok=False, fail=False):
        session = self.get(label, add=True)
        if ok:
            self.total.bump_ok()
            session.bump_ok()
        elif fail:
            self.total.bump_fail()
            session.bump_fail()
        return session

    def ok(self, label):
        return self.bump(label, ok=True)

    def fail(self, label):
        return self.bump(label, fail=True)

    def get(self, label, add=False):
        if label == "total":
            return self._total
        if label not in self.sessions:
            if add is True:
                self.sessions[label] = Session(label)
        return self.sessions[label]

    def dict(self):
        ret = dict(total=self.total().dict())
        ret["sessions"] = {
            addr: self.get(addr).dict()
            for addr in sorted(self.sessions.keys())
        }
        return ret


def exists(pathname):
    try:
        os.stat(pathname)
    except FileNotFoundError:
        return False
    return True


def is_dir(pathname):
    if exists(pathname):
        return S_ISDIR(os.stat(pathname).st_mode)
    return False


def init_cache(cache, hostname):
    hostfile = os.path.join(cache, "hostname")
    if exists(hostfile):
        with open(hostfile, "r") as ifp:
            cache_host = ifp.readline().strip()
        if cache_host != hostname:
            shutil.rmtree(cache)
    if not is_dir(cache):
        os.mkdir(cache)
    with open(hostfile, "w") as ofp:
        ofp.write(hostname + "\n")


def get_logs(hostname, pattern, cache, verbose):
    cmd = [
        "rsync",
        "-avz",
        "%s:%s/%s" % (hostname, log_dir, pattern),
        str(cache) + "/",
    ]
    stdout = check_output(cmd).decode()
    if verbose:
        click.echo(stdout)
    return cache


def update_cache(hostname, all, verbose):
    init_cache(cache_dir, hostname)
    get_logs(hostname, "current", cache_dir, verbose)
    if all:
        get_logs(hostname, "@*", cache_dir, verbose)
    return cache_dir


def log_lines(cache, all):
    pattern = os.path.join(cache, "current")
    if all:
        pattern += " " + str(cache) + "/@*"
    stdout = check_output(
        "cat " + pattern + " | tai64nlocal | sort",
        shell=True,
    ).decode()
    return stdout.split("\n")


def get_session_lines(pid, lines, index):
    ret = []
    end = re.compile(
        r".* mailfront\[" + pid + r"]: bytes in: ([0-9]+) bytes out: ([0-9]+)"
    )
    for i in range(index, index + MAX_SESSION_LINES):
        try:
            line = lines[i]
        except IndexError:
            return None, []
        if pid in line:
            ret.append(line)
        m = end.match(line)
        if m:
            return None, ret
    return "overflow", None


def alert(index, message):
    click.echo("ALERT line %d: %s" % (index, message), err=True)


def check(lines, index, verbose, quiet):  # noqa: C901
    if verbose:
        click.echo()
    sasl_auth = re.compile(r".* SASL AUTH .*")
    auth_fail = re.compile(r".* SASL AUTH [A-Z]+ failed.*")
    tls_error = re.compile(r".* sslserver: error:.*")
    smtp_response = re.compile(r".* [a-z]+\[[0-9]+\]: ([0-9\.]+) (.*)")
    auth_success = re.compile(r".* SASL AUTH LOGIN username=.*")
    auth = False
    accepted = False
    for line in lines:
        if verbose:
            click.echo(line)
        if sasl_auth.match(line):
            auth = True
        if auth_fail.match(line):
            return False, "auth_fail"
        elif tls_error.match(line):
            return False, "tls_error"
        elif auth_success.match(line):
            return True, "auth_valid"
        smtp = smtp_response.match(line)
        if smtp:
            code, message = smtp.groups()
            if code == "2.6.0":
                accepted = True
            elif code.startswith("5"):
                return False, "smtp_reject"
            elif code.startswith("4"):
                return False, "smtp_defer"
            else:
                if not quiet:
                    alert(index, "unknown SMTP response")

    if auth is False:
        if len(lines) <= 4:
            # TLS connnect w/o AUTH
            return False, "no_auth"
        if accepted is True:
            if not quiet:
                alert(index, "accepted message w/o auth")

    if accepted:
        return True, "accepted"

    return False, "undefined"


def scan(hostname, verbose=False, quiet=False, all=False, output=None):
    cache = update_cache(hostname, all, verbose)
    lines = log_lines(cache, all)
    if output:
        with open(output, "w") as ofp:
            ofp.write("\n".join(lines) + "\n")
    sessions = Sessions()
    start = re.compile(r".*sslserver: pid ([0-9]+) from (.*)")
    i = 0
    for line in lines:
        i += 1
        m = start.match(line)
        if m:
            pid = m.groups()[0]
            addr = m.groups()[1]
            err, session_lines = get_session_lines(pid, lines, i)
            if err is not None:
                if verbose:
                    click.echo(
                        "Error: session %s at line %d" % (err, i), err=True
                    )
            elif session_lines:
                valid, reason = check(session_lines, i, verbose, quiet)
                if valid:
                    sessions.ok(addr)
                else:
                    sessions.fail(addr)
                    if reason is None:
                        if quiet is False:
                            click.echo(
                                "Unknown Session Result: index=%d addr=%s pid=%s"
                                % (i, addr, pid),
                                err=True,
                            )
    return sessions
