# Inspired by: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/cd.html
import os
import sys
from glxshell.lib.path import expanduser
from glxshell.lib.path import realpath
from glxshell.lib.path import normpath
from glxshell.lib.utils import error_code_to_text

from glxshell.lib.argparse import ArgumentParser

parser_cd = ArgumentParser(
    name="cd - change the working directory",
    description="The cd utility shall change the working directory of the current shell execution environment",
)

parser_cd.add_argument(
    "directory",
    nargs="?",
    const=0,
    help="An absolute or relative pathname of the directory that shall become the new working directory. The "
    "interpretation of a relative pathname by cd depends on the -L option and the CDPATH and PWD environment "
    "variables. If directory is an empty string, the directory be come HOME environment variable.",
)
parser_cd.add_argument(
    "-P",
    dest="physical",
    action="store_true",
    default=False,
    help="Handle the operand dot-dot physically; symbolic link components shall be resolved before dot-dot components "
    "are processed",
)
parser_cd.add_argument(
    "-L",
    dest="logical",
    action="store_true",
    default=False,
    help="Handle the operand dot-dot logically; symbolic link components shall not be resolved before dot-dot "
    "components are processed ",
)


def glxsh_cd(directory=None, logical=None, physical=None, shell=None):

    if directory is None:
        directory = shell.getenv("HOME")
    if logical and physical:
        physical = False
    if not logical and not physical:
        logical = True

    if directory == "-":
        if shell.getenv("OLDPWD"):
            directory = shell.getenv("OLDPWD")
        else:
            directory = shell.getenv("PWD")

    elif directory:
        directory = expanduser(directory)

    try:
        if logical:
            os.chdir(normpath(directory))
        else:
            os.chdir(realpath(directory))

        shell.setenv("OLDPWD", shell.getenv("PWD"), 1)
        shell.setenv("PWD", os.getcwd(), 1)
        return 0

    except (Exception, ArithmeticError) as error:
        sys.stderr.write("cd: %s: '%s'\n" % (error_code_to_text(error.errno), directory))
        return 1
