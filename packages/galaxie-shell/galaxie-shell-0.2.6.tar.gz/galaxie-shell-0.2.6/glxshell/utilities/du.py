import os
import sys

from glxshell.lib.path import islink
from glxshell.lib.path import isfile
from glxshell.lib.path import joinpath
from glxshell.lib.path import getcwd
from glxshell.lib.utils import error_code_to_text

# returns both: the apparent size (number of bytes in the file) and the actual disk space the files uses.
# counts hard linked files only once
# counts symlinks the same way du does
# not use recursion
# uses st.st_blocks for disk space used, thus works only on Unix-like systems

from glxshell.lib.argparse import ArgumentParser

parser_du = ArgumentParser(
    name="du - estimate file space usage",
    description="The du utility shall write to standard output the size of the file space allocated to, and the "
                "size of the file space allocated to each subdirectory of, the file hierarchy rooted in each of "
                "the specified files.",
    synopsis=["du [-a|-s] [-kx] [-H|-L] [file...]"],
    exit_status={
        "0": "Successful completion.",
        ">0": "An error occurred."
    },
)
parser_du.add_argument(
    "-a",
    action="store_true",
    dest="a",
    help="In addition to the default output, report the size of each file not of type directory in the file "
         "hierarchy rooted in the specified file. The -a option shall not affect whether non-directories given "
         "as file operands are listed.",
)

parser_du.add_argument(
    "-H",
    action="store_true",
    dest="H",
    help="If a symbolic link is specified on the command line, du shall count the size of the file or file hierarchy "
         "referenced by the link.",
)

parser_du.add_argument(
    "-k",
    action="store_true",
    dest="k",
    default=False,
    help="Write the files sizes in units of 1024 bytes, rather than the default 512-byte units.",
)

parser_du.add_argument(
    "-L",
    action="store_true",
    dest="L",
    help="If a symbolic link is specified on the command line or encountered during the traversal of a file "
         "hierarchy, du shall count the size of the file or file hierarchy referenced by the link.",
)

parser_du.add_argument(
    "-s",
    action="store_true",
    dest="s",
    help="Instead of the default output, report only the total sum for each of the specified files.",
)

parser_du.add_argument(
    "-x",
    action="store_true",
    dest="x",
    help="When evaluating file sizes, evaluate only those files that have the same device as the file "
         "specified by the file operand.",
)

parser_du.add_argument(
    "file",
    dest="files",
    nargs="*",
    help="The pathname of a file whose size is to be written. If no file is specified, the current directory "
         "shall be used.",
)

def glxsh_du(a, H, k, L, s, x, files):
    exit_code = 0
    if k:
        byte_unit = 1024
    else:
        byte_unit = 512

    if not files:
        files = [getcwd()]

    try:
        for path in files:
            if os.access(path, os.R_OK):
                if islink(path):
                    sys.stdout.write("%d %s\n" % (os.lstat(path).st_size, path))
                if isfile(path):
                    sys.stdout.write("%d %s\n" % (os.lstat(path).st_blocks * 512 / byte_unit,  path))
                have = []
                for directory_path, directory_names, filenames in os.walk(path):
                    for f in filenames:
                        fp = joinpath(directory_path, f)
                        if islink(fp):
                            sys.stdout.write("%d %s\n" % (os.lstat(fp).st_size, fp))
                            continue
                        st = os.lstat(fp)
                        if st.st_ino in have:
                            continue  # skip hardlinks which were already counted
                        have.append(st.st_ino)
                        sys.stdout.write("%d %s\n" % (st.st_blocks * 512 / byte_unit, fp))
                    for d in directory_names:
                        dp = joinpath(directory_path, d)
                        if islink(dp):
                            sys.stdout.write("%d %s\n" % (os.lstat(dp).st_size, dp))
            else:
                sys.stderr.write("du: %s: '%s'\n" % (error_code_to_text(13), path))
    except OSError as error:
        sys.stderr.write("du: %s\n" % (error_code_to_text(error.errno)))
        exit_code += 1
    except KeyboardInterrupt:
        sys.stdout.write("\n")

    return exit_code


