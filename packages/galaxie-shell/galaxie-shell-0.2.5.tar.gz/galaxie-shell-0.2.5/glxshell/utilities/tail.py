import sys
from glxshell.lib.argparse import ArgumentParser
from glxshell.lib.argparse import FileType
from glxshell.lib.utils import error_code_to_text
from typing import Iterator
from time import sleep

parser_tail = ArgumentParser(
    name="tail - copy the last part of a file",
    synopsis=["tail [-f] [-c number|-n number] [file]"],
    description="The tail utility shall copy its input file to the standard output beginning at a designated place."
                "\n\n"
                "Copying shall begin at the point in the file indicated by the -c number or -n number options. "
                "The option-argument number shall be counted in units of lines or bytes, according to the options "
                "-n and -c. Both line and byte counts start from 1.",

)

parser_tail.add_argument(
    "-f",
    dest="f",
    action="store_true",
    default=False,
    help="If the input file is a regular file or if the file operand specifies a FIFO, do not terminate after the "
         "last line of the input file has been copied, but read and copy further bytes from the input file when they "
         "become available. If no file operand is specified and standard input is a pipe or FIFO, the -f option shall "
         "be ignored. If the input file is not a FIFO, pipe, or regular file, it is unspecified whether or not the -f "
         "option shall be ignored.",
)

parser_tail.add_argument(
    "-c",
    dest="c",
    type=str,
    help="The origin for counting shall be 1; that is, -c +1 represents the first byte of the file, -c -1 the last.",
)

parser_tail.add_argument(
    "-n",
    dest="n",
    type=str,
    help="This option shall be equivalent to -c number, except the starting location in the file shall be measured "
         "in lines instead of bytes. The origin for counting shall be 1; that is, -n +1 represents the first line "
         "of the file, -n -1 the last.",
)

parser_tail.add_argument(
    "file",
    nargs="*",
    type=FileType("r"),
    help="A pathname of an input file. If no file operand is specified, the standard input shall be used.",
)


def glxsh_tail(c, f, n, files):
    """
    The tail utility shall copy its input file to the standard output beginning at a designated place.

    Copying shall begin at the point in the file indicated by the -c number or -n number options.
    The option-argument number shall be counted in units of lines or bytes, according to the options -n and -c.
    Both line and byte counts start from 1.

    Tails relative to the end of the file may be saved in an internal buffer, and thus may be limited in length.
    Such a buffer, if any, shall be no smaller than {LINE_MAX}*10 bytes.

    :param files: A pathname of an input file. If no file operand is specified, the standard input shall be used.
    :type files: list or None
    """

    def follow(file, sleep_sec=0.1) -> Iterator[str]:
        """ Yield each line from a file as they are written.
        `sleep_sec` is the time to sleep after empty reads. """
        line = ''
        while True:
            tmp = file.readline()
            if tmp is not None:
                line += tmp
                if line.endswith("\n"):
                    yield line
                    line = ''
            elif sleep_sec:
                sleep(sleep_sec)



    try:
        if files is None or files == []:
            files = ["-"]
        if f:
            for file in files:
                if file == "-":
                    file = sys.stdin
                with open(file, "r") as fd:
                    loglines = follow(fd)
                    # iterate over the generator
                    for line in loglines:
                        sys.stdout.write("%s" % line)

            return 0
    except OSError as error:
        sys.stderr.write("tail: %s\n" % (error_code_to_text(error.errno)))
        return 1
    except KeyboardInterrupt:
        sys.stdout.write("\n")
        return 0
