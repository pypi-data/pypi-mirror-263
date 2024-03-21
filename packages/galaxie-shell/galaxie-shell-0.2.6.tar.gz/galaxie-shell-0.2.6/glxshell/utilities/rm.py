# Inspired by: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/rm.html

import os
import sys
from glxshell.lib.argparse import ArgumentParser
from glxshell.lib.utils import error_code_to_text
from glxshell.lib.path import joinpath


parser_rm = ArgumentParser(
    name="rm - remove directory entries",
    description="The rm utility shall remove the directory entry specified by each file argument.\n"
    "\n"
    "If either of the files dot or dot-dot are specified as the basename portion of an operand (that is, "
    "the final pathname component) or if an operand resolves to the root directory, rm shall write a "
    "diagnostic message to standard error and do nothing more with such operands.",
)
parser_rm.add_argument(
    "-i",
    dest="interactive",
    action="store_true",
    help="Prompt for confirmation as described previously. Any previous occurrences of the -f option shall be ignored.",
)
parser_rm.add_argument(
    "-R",
    "-r",
    dest="recursive",
    action="store_true",
    help="Remove file hierarchies. See the DESCRIPTION.",
)
parser_rm.add_argument(
    "-f",
    dest="force",
    action="store_true",
    help="Do not prompt for confirmation. Do not write diagnostic messages or modify the exit status in the case of "
    "no file operands, or in the case of operands that do not exist. Any previous occurrences of the -i option "
    "shall be ignored.",
)
parser_rm.add_argument(
    "file",
    nargs="+",
    help="A pathname of a directory entry to be removed.",
)


def glxsh_rm(file=None, recursive=None, interactive=None, force=None):
    exit_code = 0
    if force:
        interactive = False

    def _rm(path):
        try:
            os.remove(path)
            return 0
        except OSError as error:
            sys.stderr.write("rm: %s: '%s'\n" % (error_code_to_text(error.errno), path))
            return 1
        except (Exception, BaseException) as error:
            sys.stderr.write("chmod: %s: '%s'\n" % (error, path))
            return 1

    for path in file:
        if recursive:
            for dirpath, dirnames, filenames in os.walk(path):
                for dname in dirnames:
                    if interactive:
                        if input("do you want to remove %s directory ? (Y/n)" % joinpath(dirpath, dname)).upper().startswith("Y"):
                            exit_code += _rm(joinpath(dirpath, dname))
                    else:
                        exit_code += _rm(joinpath(dirpath, dname))
                for fname in filenames:
                    if interactive:
                        if input("do you want to remove %s file ? (Y/n)" % joinpath(dirpath, fname)).upper().startswith("Y"):
                            exit_code += _rm(joinpath(dirpath, fname))
                    else:
                        exit_code += _rm(joinpath(dirpath, fname))

        else:
            if interactive:
                if input("do you want to remove %s file ? (Y/n)" % path).upper().startswith("Y"):
                    exit_code += _rm(path)
            else:
                exit_code += _rm(path)

    return 1 if exit_code else 0
