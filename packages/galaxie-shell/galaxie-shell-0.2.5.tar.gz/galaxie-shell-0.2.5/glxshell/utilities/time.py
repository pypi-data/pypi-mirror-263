# inspired by: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/time.html
import sys

from glxshell.lib.argparse import ArgumentParser

parser_time = ArgumentParser(
    name="time - time a simple command",
    description="The time utility shall invoke the utility named by the utility operand with arguments supplied as "
                "the argument operands and write a message to standard error that lists timing statistics for the "
                "utility. ",
    synopsis=["time [-p] utility [argument...]"],
    exit_status={
        "1-125": "An error occurred in the time utility.",
        "126": "The utility specified by utility was found but could not be invoked.",
        "127": "The utility specified by utility could not be found.",
    }
)
parser_time.add_argument(
    "-p",
    dest="p",
    action="store_true",
    help="Write the timing output to standard error",
)

parser_time.add_argument(
    "utility",
    nargs="?",
    help="The name of a utility that is to be invoked.",
)

parser_time.add_argument(
    "argument",
    nargs="?",
    help="Any string to be supplied as an argument when invoking the utility named by the utility operand.",
)

def glxsh_time(p=None, utility=None, argument=None, line=None, shell=None):
    from time import time
    from os import times


    exit_code = 0


    en_time = times()
    start = time()

    exit_code = shell.onecmd(line)


    en_time = times()

    sys.stderr.write("real %f\nuser %f\nsys %f\n" % (time() - start, en_time.user, en_time.system ))
    sys.stderr.flush()

    return exit_code