# inspired by: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/head.html

import sys
from glxshell.lib.argparse import ArgumentParser

parser_head = ArgumentParser(
    name="head - copy the first part of",
    description="The head utility shall copy its input files to the standard output, ending the output for each file "
    "at a designated point. ",
)

parser_head.add_argument(
    "file",
    nargs="*",
    help="A pathname of an input file. If no file operands are specified, the standard input shall be used.",
)

parser_head.add_argument(
    "-n",
    dest="number",
    type=int,
    default=10,
    help="The first number lines of each input file shall be copied to standard output. ",
)


def glxsh_head(files, number=10):
    """
    head - copy the first part of files

    :param number: The first number lines of each input file shall be copied to standard output.
    :type number: int
    :param files: A list where each item is pathname of an input file.
    :type files: list or None
    :return: 0 -> Successful completion, 1 -> An error occurred, 130 -> KeyboardInterrupt
    """
    if isinstance(number, int) and number < 1:
        return 0

    if files is None or not isinstance(files, list) or files == []:
        files = ["-"]

    def read_stdin():
        stdin_count = 1
        while stdin_count <= number:
            data = sys.stdin.readline()
            if not data:
                break
            yield data
            stdin_count += 1

    try:
        count = 0
        for file in files:
            filename = file
            if file == "-":
                filename = "standard input"
            if count == 0 and len(files) > 1:
                sys.stdout.write("==> %s <==\n" % filename)
            elif count > 0:
                sys.stdout.write("\n==> %s <==\n" % filename)
            if file == "-":
                try:
                    for piece in read_stdin():
                        sys.stdout.write(piece)
                except KeyboardInterrupt:
                    sys.stdout.write("\n")
                    return 130
            else:
                with open(file) as f:
                    for _ in range(number):
                        line = f.readline()
                        if not line:
                            break
                        sys.stdout.write(line)
            count += 1
        return 0
    except (Exception, ArithmeticError) as error:  # pragma: no cover
        sys.stderr.write("head: %s\n" % error)
        return 1
