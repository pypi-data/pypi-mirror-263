# Inspired by: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/chmod.html
import os
import sys
import stat
from glxshell.lib.glob import glob
from glxshell.lib.argparse import ArgumentParser
from glxshell.lib.utils import error_code_to_text
from glxshell.lib.symbolic_mode import symbolic_mode

parser_chmod = ArgumentParser(
    name="chmod - change the file modes",
    description="""The chmod utility shall change any or all of the file mode bits of the file named by each file operand in the way specified by the mode operandself.

Only a process whose effective user ID matches the user ID of the file, or a process with appropriate privileges, shall be permitted to change the file mode bits of a file.
""",
)
parser_chmod.add_argument(
    "-R",
    dest="recursive",
    action="store_true",
    default=False,
    help="Recursively change file mode bits.",
)
parser_chmod.add_argument(
    "mode",
    dest="mode",
    help="Represents the change to be made to the file mode bits of each file named by one of the file operands",
)
parser_chmod.add_argument(
    "file",
    dest="file",
    nargs="+",
    help="A pathname of a file whose file mode bits shall be modified.",
)


def glxsh_chmod(recursive=None, mode=None, file=None):
    exit_code = 0
    
    def _chmod(path, mode):
        try:
            # symbolic_mode("=x", mode=0444, umask=0700) == 0411
            os.chmod(path, mode)
            return 0
        except OSError as error:
            sys.stderr.write("chmod: %s: '%s'\n" % (error_code_to_text(error.errno), path))
            return 1
        except (Exception, BaseException) as error:
            sys.stderr.write("chmod: %s: '%s'\n" % (error, path))
            return 1

    for path in file:
        if recursive:
            dir_scan = glob("%s/**/*" % path)
        else:
            dir_scan = glob(path)
        for f in dir_scan:
            # TODO fix mono non existant file or directory
            # try:
            #     os.stat(path)
            # except OSError as error:
            #     exit_code += 1
            #     sys.stderr.write("chmod: %s: '%s'\n" % (error_code_to_text(error.errno), path))
            #
            if stat.S_ISDIR(os.stat(f)[0]):
                try:
                    mode = symbolic_mode(mode, mode=os.stat(f).st_mode, umask=os.umask(0), isdir=1)
                except TypeError:
                    pass
            else:
                try:
                    mode = symbolic_mode(mode, mode=os.stat(f).st_mode, umask=os.umask(0), isdir=0)
                except TypeError:
                    pass
            if not isinstance(mode, int):
                mode = int(mode, 8)
            exit_code += _chmod(f, mode)

    return 1 if exit_code else 0
