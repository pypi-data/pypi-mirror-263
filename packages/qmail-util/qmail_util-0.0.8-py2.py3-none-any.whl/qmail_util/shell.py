# shell completion

import os
import os.path
import sys

import click


def _shell_completion(ctx, option, shell):
    """output shell completion code"""

    if shell is None:
        return
    elif shell == "[auto]":
        if "SHELL" in os.environ:
            shell = os.path.basename(os.environ["SHELL"])
        elif "ZSH_VERSION" in os.environ:
            shell = "zsh"

    if shell not in ["bash", "zsh"]:
        raise RuntimeError("cannot determine shell")

    cli = os.path.basename(ctx.command_path)

    if shell == "bash":
        click.echo("Writing file ~/." + cli + "-complete.bash...")
        os.system("_%s_COMPLETE=bash_source %s >~/.%s-complete.bash" % (cli.upper(), cli, cli))
        click.echo("Source this file from ~/.bashrc")
        click.echo("ex: . ~/.%s-complete.bash" % (cli,))

    elif shell == "zsh":
        click.echo("Writing file ~/.%s-complete.zsh..." % (cli,))
        os.system("_%s_COMPLETE=zsh_source %s >~/.%s-complete.zsh" % (cli.upper(), cli, cli))
        click.echo("Source this file from ~/.zshrc")
        click.echo("ex: . ~/.%s-complete.zsh" % (cli,))

    sys.exit(0)
