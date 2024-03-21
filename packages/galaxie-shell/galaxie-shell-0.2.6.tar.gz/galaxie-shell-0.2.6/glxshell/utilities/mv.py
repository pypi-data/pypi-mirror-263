# inspired by: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/mv.html

import os
import sys
from glxshell.lib.path import exists
from glxshell.lib.argparse import ArgumentParser

parser_mv = ArgumentParser(
    name="mv - move files",
    description="The mv utility shall move the file named by the source_file operand to "
    "the destination specified by the target_file. This first synopsis form is assumed when the final "
    "operand does not name an existing directory and is not a symbolic link referring to an existing "
    "directory. In this case, if source_file names a non-directory file and target_file ends with a "
    "trailing <slash> character, mv shall treat this as an error and no source_file operands will be "
    "processed.",
)

parser_mv.add_argument(
    "source_file",
    nargs="?",
    help="A pathname of a file or directory to be moved.",
)

parser_mv.add_argument(
    "target_file",
    nargs="?",
    help="A new pathname for the file or directory being moved.",
)

parser_mv.add_argument(
    "target_dir",
    nargs="?",
    help="A pathname of an existing directory into which to move the input files.",
)

parser_mv.add_argument(
    "-f",
    dest="force",
    action="store_true",
    default=False,
    help="Do not prompt for confirmation if the destination path exists. "
    "Any previous occurrence of the -i option is ignored.",
)

parser_mv.add_argument(
    "-i",
    dest="interactive",
    action="store_true",
    default=False,
    help="Prompt for confirmation if the destination path exists. Any previous occurrence of the -f option is ignored.",
)


def glxsh_mv(source_file=None, target_file=None, target_dir=None, force=None, interactive=None):
    if interactive and exists(target_file):
        sys.stdout.write("do you want to overwrite %s file ? (Y/n) " % target_file)
        sys.stdout.flush()
        if sys.stdin.readline().upper().startswith("N"):
            return 0
    try:
        if os.access(source_file, os.F_OK):
            os.rename(source_file, target_file)
            return 0
        else:
            return 1
    except Exception as error:
        sys.stderr.write("mv: %s\n" % error)
        return 1

