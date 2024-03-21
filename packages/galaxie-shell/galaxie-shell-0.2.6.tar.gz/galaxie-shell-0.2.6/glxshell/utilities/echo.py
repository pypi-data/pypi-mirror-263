# Inspired by: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/echo.html
import sys
from glxshell.lib.argparse import ArgumentParser

parser_echo = ArgumentParser(
    name="echo - write arguments to standard output",
    description="The echo utility writes its arguments to standard output, followed by a <newline>. "
                "If there are no arguments, only the <newline> is written.",
)
parser_echo.add_argument(
    "-n",
    dest="newline",
    action="store_true",
    help="Suppress the <newline> that would otherwise follow the final argument in the output.",
)
parser_echo.add_argument(
    "string",
    nargs="*",
    type=str,
    help="A string to be written to standard outputself.\n",
)


def glxsh_echo(**kwargs):
    shell = kwargs.get("shell", None)
    newline = kwargs.get("newline", False)
    string = kwargs.get("string", "")

    try:
        value_to_return = str(string)
        if string.startswith('"') and string.endswith('"'):
            value_to_return = string[1:][:-1]
            for value in value_to_return.split(" "):
                if value.startswith("$"):
                    value_to_return = value_to_return.replace(value, shell.environ.get(value.replace("$", ""), ""))
        if string.startswith("$") and " " not in string:
            value_to_return = string.replace(string, shell.environ.get(string.replace("$", ""), ""))
        sys.stdout.write(value_to_return)

        if not newline:
            sys.stdout.write("\n")
        return 0

    except (Exception, BaseException) as error:
        sys.stderr.write(error)
        # stderr.write("echo: %s: '%s'\n" % (error_code_to_text(error.errno), string))
        return 1
