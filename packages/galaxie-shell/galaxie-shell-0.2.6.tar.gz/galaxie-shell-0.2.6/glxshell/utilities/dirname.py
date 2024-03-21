# inspired by: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/dirname.html
import sys
from glxshell.lib.argparse import ArgumentParser
from glxshell.lib.path import dirname

parser_dirname = ArgumentParser(
    name="dirname - return the directory portion of a pathname",
    description="The string operand shall be treated as a pathname, as defined in XBD Pathname. The string string "
    "shall be converted to the name of the directory containing the filename corresponding to the last "
    "pathname component in string.",
)
parser_dirname.add_argument(
    "string",
    nargs="?",
    const=0,
    help="A string",
)


def glxsh_dirname(string=None):
    try:
        sys.stdout.write("%s\n" % dirname(string))
        return 0
    except (Exception, ArithmeticError) as error:  # pragma: no cover
        sys.stderr.write("dirname: %s\n" % error)
        return 1
