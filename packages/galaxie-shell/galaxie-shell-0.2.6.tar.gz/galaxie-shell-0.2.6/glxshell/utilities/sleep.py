import time
import sys
from glxshell.lib.argparse import ArgumentParser

parser_sleep = ArgumentParser(
    name="sleep - suspend execution for an interval",
    description="The sleep utility shall suspend execution for at least the integral number of seconds specified by "
    "the time operand. ",
)
parser_sleep.add_argument(
    "time",
    default=0,
    help="A non-negative decimal integer or float specifying the number of seconds for which to suspend execution.",
)


def glxsh_sleep(sec):
    exit_code = 0

    def string_to_numeric_if_possible(x):
        try:
            val = float(x)
            return int(val) if val == int(val) else val
        except (TypeError, ValueError):
            return x

    try:
        time.sleep(string_to_numeric_if_possible(sec))
    except (Exception, ArithmeticError) as error:
        sys.stderr.write("sleep: %s\n" % error)
        exit_code += 1
    except KeyboardInterrupt:  # pragma: no cover
        sys.stdout.write("\n")
        exit_code += 1

    return exit_code
