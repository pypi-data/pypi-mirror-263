"""Console script for qmail_util."""

import json
import sys

import click
import click.core

from .exception_handler import ExceptionHandler
from .main import scan
from .shell import _shell_completion
from .version import __timestamp__, __version__

header = __name__.split(".")[0] + " v" + __version__ + " " + __timestamp__


def _ehandler(ctx, option, debug):
    ctx.obj = dict(ehandler=ExceptionHandler(debug))
    ctx.obj["debug"] = debug


def _version(ctx, option, version):
    if version:
        print(header)
        sys.exit(0)


@click.group("qmu", context_settings={"auto_envvar_prefix": "QMU"})
@click.option(
    "-d",
    "--debug",
    is_eager=True,
    is_flag=True,
    callback=_ehandler,
    help="debug mode",
)
@click.option("--version", is_flag=True, is_eager=True, callback=_version, help="show version info")
@click.option("-q", "--quiet", is_flag=True, help="suppress error output")
@click.option("-v", "--verbose", is_flag=True, help="output log data")
@click.option(
    "-f", "--format", type=click.Choice(["json", "text"]), help="output format"
)
@click.option(
    "--shell-completion",
    is_flag=False,
    flag_value="[auto]",
    callback=_shell_completion,
    help="configure shell completion",
)
@click.pass_context
def cli(ctx, debug, shell_completion, quiet, verbose, format):
    """qmail-util top-level help"""

    class Options:
        def __init__(self, **kwargs):
            for k, v in kwargs.items():
                setattr(self, k, v)

    ctx.obj = Options(quiet=quiet, verbose=verbose, format=format)


def output_session(session, count, ip_only):
    if count is None or session.fail < count:
        return
    if ip_only:
        click.echo(str(session.addr))
    else:
        click.echo(str(session))


@cli.command('smtpsd')
@click.option("-a", "--all", is_flag=True, help="all logs")
@click.option("-t", "--total", is_flag=True, help="output totals")
@click.option("-i", "--ip-only", is_flag=True, help="output IP addresses only")
@click.option("-c", "--count", type=int, help="failure threshold")
@click.option("-o", "--output", help="output log filename")
@click.argument("hostname")
@click.pass_obj
def smtpsd(opt, hostname, all, total, count, output, ip_only):
    """scan TLS SMTP daemon connection logs"""
    sessions = scan(hostname, opt.verbose, opt.quiet, all=all, output=output)
    if opt.format == "json":
        click.echo(json.dumps(sessions.dict(), indent=2) + "\n")
    else:
        for addr in sorted(sessions.keys()):
            session = sessions.get(addr)
            output_session(session, count, ip_only)
        if total:
            output_session(sessions.total, None, ip_only)


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
