import sys
from glxshell.lib.argparse import ArgumentParser
from glxshell.lib.argparse import FileType

parser_cat = ArgumentParser(
    name="cat - concatenate and print files",
    description="The cat utility shall read files in sequence and shall write their contents to the standard output "
    "in the same sequence.",
)
parser_cat.add_argument(
    "file",
    nargs="*",
    type=FileType("r"),
    help="A pathname of an input file. If no file operands are specified, the standard input shall be used. If a file "
    "is '-', the cat utility shall read from the standard input at that point in the sequence. The cat utility "
    "shall not close and reopen standard input when it is referenced in this way, but shall accept multiple "
    "occurrences of '-' as a file operand.",
)

parser_cat.add_argument(
    "-u",
    dest="update",
    action="store_true",
    default=False,
    help="ignored",
)


def glxsh_cat(files):
    """
    The cat utility shall read files in sequence and shall write their contents to the standard output in the same
    sequence.

    If no file operands are specified, the standard input shall be used.

    If a file is '-', the cat utility shall read from the standard input at that point in the sequence.
    The cat utility shall not close and reopen standard input when it is referenced in this way, but shall
    accept multiple occurrences of '-' as a file operand.

    :param files: A pathname of an input file.
    :type files: list or None
    """
    def read_file_in_chunks(file_object, chunk_size=3072):
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data

    def read_stdin(file_object):
        while True:
            data = file_object.readline()
            if not data:
                break
            yield data

    try:
        if files is None or files == []:
            files = ["-"]
        for file in files:
            if file == "-":
                for piece in read_stdin(sys.stdin):
                    sys.stdout.write(piece)
            else:
                with open(file, "r") as f:
                    for piece in read_file_in_chunks(f):
                        sys.stdout.write(piece)
        return 0
    except (Exception, ArithmeticError) as error:  # pragma: no cover
        sys.stderr.write("cat: %s\n" % error)
        return 1
