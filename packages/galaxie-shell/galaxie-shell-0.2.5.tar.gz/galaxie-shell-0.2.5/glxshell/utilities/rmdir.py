# Inspired by: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/rmdir.html
import os
import sys
from glxshell.lib.argparse import ArgumentParser
from glxshell.lib.utils import error_code_to_text
from glxshell.lib.path import exists

parser_rmdir = ArgumentParser(
    name="rmdir - remove directories",
    description="The rmdir utility shall remove the directory entry specified by each dir operand.\n\n"
    "Directories shall be processed in the order specified. If a directory and a subdirectory of that "
    "directory are specified in a single invocation of the rmdir utility, the application shall specify "
    "the subdirectory before the parent directory so that the parent directory will be empty when the "
    "rmdir utility tries to remove it.",
)
parser_rmdir.add_argument(
    "dir",
    dest="dir",
    nargs="*",
    help="A pathname of an empty directory to be removed.",
)

parser_rmdir.add_argument(
    "-p",
    dest="parents",
    action="store_true",
    default=False,
    help="Remove all directories in a pathname.",
)


def glxsh_rmdir(directories=None, parents=False):
    exit_code = 0

    def rmdir(d):
        try:
            os.rmdir(path=d)
            return 0
        except (Exception, ArithmeticError) as error:
            sys.stderr.write("rmdir: %s: '%s'\n" % (error_code_to_text(error.errno), d))
            return 1

    for directory in directories:
        if exists(directory) and parents:
            for path, _, files in os.walk(directory, False):
                for f in files:
                    os.unlink(path + "/" + f)
                exit_code += rmdir(path)
        else:
            exit_code += rmdir(directory)

    return 1 if exit_code else 0
