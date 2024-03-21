import sys

from glxshell.lib.argparse import ArgumentParser

parser_exit = ArgumentParser(name="exit", description="exit shell with a given exit code")
parser_exit.add_argument(
    "code",
    nargs="*",
    type="int",
    help="exit code",
)


def glxsh_exit(*args, **kwargs):
    shell = kwargs.get("shell", None)
    code = kwargs.get("code", None)

    if code is None or not code:
        code = 0
    else:
        code = code[0]
    if shell:
        shell.exit_code = code
        sys.exit(code)
        # shell.do_EOF()
    else:
        return code

