# inspired by: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/mkdir.html

import sys
from glxshell.lib.argparse import ArgumentParser
from glxshell.lib.utils import error_code_to_text
from glxshell.lib.path import sep
from glxshell.lib.path import joinpath

parser_mkdir = ArgumentParser(
    name="mkdir - make directories",
    description="The mkdir utility shall create the directories specified by the operands",
)
parser_mkdir.add_argument(
    "-p",
    dest="parents",
    action="store_true",
    help="Create any missing intermediate pathname components.",
)
parser_mkdir.add_argument(
    "-m",
    dest="mode",
    nargs="?",
    type=str,
    default="755",
    help="Set the file permission bits of the newly-created directory to the specified mode value.",
)

parser_mkdir.add_argument("dir", nargs="+", help="A pathname of a directory to be created.")


def glxsh_mkdir(directories=None, parents=False, mode="755"):
    exit_code = 0

    def make_directory(path, path_mode):
        try:
            from os import mkdir
            try:
                mkdir(path=path, mode=path_mode)
            except TypeError:
                mkdir(path)
        except ImportError as error:
            sys.stderr.write("mkdir: '%s'\n" % error)
        except OSError as error:
            sys.stderr.write("mkdir: '%s': %s\n" % (path, error_code_to_text(error.errno)))
            return 1
        return 0

    for directory in directories:
        if parents:
            if directory.startswith(sep):
                directory_to_create = sep
            else:
                directory_to_create = ""
            for sub_directory in directory.split(sep):
                if directory_to_create == sep:
                    directory_to_create = "%s%s" % (directory_to_create, sub_directory)
                elif directory_to_create != "" and sub_directory != "":
                    directory_to_create = joinpath(directory_to_create, sub_directory)
                else:
                    if sub_directory == "":
                        continue
                    elif sub_directory == ".":
                        directory_to_create = "."
                        continue
                    elif sub_directory == "..":
                        directory_to_create = ".."
                        continue
                    else:
                        directory_to_create = sub_directory
                exit_code += make_directory(directory_to_create, mode)

        else:
            exit_code += make_directory(directory, mode)

    return 1 if exit_code else 0
