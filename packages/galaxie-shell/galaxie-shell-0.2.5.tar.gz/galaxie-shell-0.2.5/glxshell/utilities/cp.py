# https://pubs.opengroup.org/onlinepubs/9699919799/utilities/cp.html

import sys

from glxshell.lib.argparse import ArgumentParser
from glxshell.lib.path import exists
from glxshell.lib.utils import error_code_to_text

parser_cp = ArgumentParser(
    name="cp - copy files",
    description="The first synopsis form is denoted by two operands, neither of which are existing files of type "
    "directory. The cp utility shall copy the contents of source_file (or, if source_file is a file of "
    "type symbolic link, the contents of the file referenced by source_file) to the destination path "
    "named by target_file.",
    exit_status={
        "0": "The utility executed successfully and all requested changes were made.",
        ">0": "An error occurred."
        },
)

parser_cp.add_argument(
    "-f",
    dest="force",
    action="store_true",
    help="If a file descriptor for a destination file cannot be obtained, as described in step 3.a.ii., attempt to "
    "unlink the destination file and proceed.",
)

parser_cp.add_argument(
    "-i",
    dest="interactive",
    action="store_true",
    help="Write a prompt to standard error before copying to any existing non-directory destination file.",
)

parser_cp.add_argument(
    "source_file",
    nargs="+",
    help="A pathname of a file to be copied. If a source_file operand is '-', it shall refer to a file named -; "
    "implementations shall not treat it as meaning standard input. target_file",
)

parser_cp.add_argument(
    "target_file",
    help="A pathname of an existing or nonexistent file, used for the output when a single file is copied. If a "
    "target_file operand is '-', it shall refer to a file named -; implementations shall not treat it as meaning "
    "standard output.",
)


def glxsh_cp(source_file, target_file, interactive=False):
    try:
        with open(source_file, "r") as source_file_descriptor:
            pass
    except (Exception, ArithmeticError) as error:
        sys.stderr.write("cp: %s: '%s'\n" % (error_code_to_text(error.errno), source_file))
        return 1

    if interactive and exists(target_file):
        if input("do you want to overwrite %s file ? (Y/n)" % target_file).upper().startswith("N"):
            return 0

    try:
        with open(target_file, "w") as target_file_descriptor:
            pass
    except (Exception, ArithmeticError) as error:
        sys.stderr.write("cp: %s: '%s'\n" % (error_code_to_text(error.errno), target_file))
        return 1

    try:
        with open(source_file, "r") as source_file_descriptor:
            with open(target_file, "w") as target_file_descriptor:
                target_file_descriptor.write(source_file_descriptor.read())
        return 0
    except (Exception, ArithmeticError) as error:
        sys.stderr.write("cp: %s:\n" % (error_code_to_text(error.errno)))
        return 1

