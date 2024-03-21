# inspired by: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/basename.html

import sys

from glxshell.lib.argparse import ArgumentParser
from glxshell.lib.path import basename

parser_basename = ArgumentParser(
    name="basename - return non-directory portion of a pathname",
    prog="basename",
    description="Print string with any leading directory components removed. If specified, also remove a "
                "trailing suffix.",
)
parser_basename.add_argument(
    "string",
    type=str,
    nargs="?",
    default=None,
    help="a string",
)

parser_basename.add_argument(
    "suffix",
    nargs="?",
    default=None,
    help="a string",
)


def glxsh_basename(string=None, suffix=None):
    """
    Print ``string`` with any leading directory components removed. If specified, also remove a trailing ``suffix``.

    :param string: a string
    :type string: str
    :param suffix: a string
    :type suffix: str
    :return: 0 if successful completion, >0 if an error occurred.
    :rtype: int
    """
    try:
        sys.stdout.write("%s\n" % basename(string, suffix))
        return 0
    except (Exception, ArithmeticError) as error:  # pragma: no cover
        sys.stderr.write("basename: %s\n" % error)
        return 1
