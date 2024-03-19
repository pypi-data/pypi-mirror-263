# inspired by: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/pwd.html
import os
import sys
from glxshell.lib.path import normpath
from glxshell.lib.path import realpath
from glxshell.lib.argparse import ArgumentParser

parser_pwd = ArgumentParser(
    name="pwd - return working directory name",
    description="The pwd utility shall write to standard output an absolute pathname of the current working "
    "directory, which does not contain the filenames dot or dot-dot.",
)
parser_pwd.add_argument(
    "-L",
    dest="logical",
    action="store_true",
    default=False,
    help="Print the value of $PWD if it names the current working directory",
)
parser_pwd.add_argument(
    "-P",
    dest="physical",
    action="store_true",
    default=False,
    help="Print the physical directory, without any symbolic links",
)


def glxsh_pwd(logical=None, physical=None):
    """
    The pwd utility shall write to standard output an absolute pathname of the current working directory, 
    which does not contain the filenames dot or dot-dot.

    If both ``logical`` and ``physical`` are specified, the last one shall apply. 
    If neither ``logical`` nor ``physical`` is specified, the pwd utility shall behave as if ``logical`` had 
    been specified.

    :param logical: If the PWD environment variable contains an absolute pathname of the current directory and the pathname does not contain any components that are dot or dot-dot
    :type logical: bool
    :param physical: The pathname written to standard output shall not contain any components that refer to files of type symbolic link
    :type physical: bool
    """
    if not logical and not physical:
        logical = True
    try:
        if logical:
            sys.stdout.write("%s\n" % normpath(os.getcwd()))
        else:
            sys.stdout.write("%s\n" % realpath(os.getcwd()))
        return 0
    except (Exception, ArithmeticError) as error:  # pragma: no cover
        sys.stderr.write("pwd: %s\n" % error)
        return 1
