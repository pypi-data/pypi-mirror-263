import sys

from glxshell.lib.argparse import ArgumentParser
from glxshell.lib.argparse import FileType
from glxshell.lib.utils import error_code_to_text

parser_tee = ArgumentParser(
    name="tee - duplicate standard input",
    synopsis=["tee [-ai] [file...]"],
    description="The tee utility shall copy standard input to standard output, making a copy in zero or more files. "
                "The tee utility shall not buffer output."
                "\n\n"
                "If the -a option is not specified, output files shall be written.",
    exit_status={
        "0": "The standard input was successfully copied to all output files.",
        ">0": "An error occurred.",
    }
)

parser_tee.add_argument(
    "-a",
    dest="a",
    action="store_true",
    default=False,
    help="Append the output to the files.",
)

parser_tee.add_argument(
    "-i",
    dest="i",
    action="store_true",
    default=False,
    help="Ignore the SIGINT signal.",
)

parser_tee.add_argument(
    "file",
    nargs="*",
    type=FileType("r"),
    help="A pathname of an output file. If a file operand is '-', it refer to a file named '-'",
)


def glxsh_tee(a=None, i=None, files=None):
    a: bool
    i: bool
    files: list

    if a is True:
        mode = "a"
    else:
        mode = "w"

    exit_code = 0
    opened_files = []
    if files:
        for file in files:
            try:
                opened_files.append(open(file, mode))
            except (Exception, BaseException) as error:  # pragma: no cover
                sys.stderr.write("tee: %s: '%s'\n" % (error_code_to_text(error.errno), file))
                exit_code += 1

    def read_stdin(file_object):
        while True:
            data = file_object.readline()
            if not data:
                break
            yield data

    def process_data(data):
        sys.stdout.write(piece)
        for opened_file in opened_files:
            opened_file.write(piece)
            opened_file.flush()

    def close_data():
        try:
            for opened_file in opened_files:
                opened_file.flush()
                opened_file.close()
            return 0
        except (Exception, BaseException) as err:  # pragma: no cover
            sys.stderr.write("tee: %s: '%s'\n" % (error_code_to_text(err.errno), file))
            return 1

    try:
        for piece in read_stdin(sys.stdin):
            process_data(piece)
    except KeyboardInterrupt:
        exit_code += close_data()
        return 1 if exit_code else 0
    finally:
        exit_code += close_data()
        return 1 if exit_code else 0
