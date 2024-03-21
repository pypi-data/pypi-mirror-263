# https://pubs.opengroup.org/onlinepubs/9699919799/utilities/tty.html

import os
import sys
from glxshell.lib.argparse import ArgumentParser
from glxshell.lib.utils import error_code_to_text

parser_tty = ArgumentParser(
    name="tty - return user's terminal name",
    description="The tty utility shall write to the standard output the name of the terminal that is open as standard "
    "input.",
)


def glxsh_tty():
    try:
        sys.stdout.write("%s\n" % os.ttyname(sys.stdin.fileno()))
        return 0
    except OSError:
        sys.stdout.write("not a tty\n")
        return 1
    except (Exception, ArithmeticError) as error:  # pragma: no cover
        sys.stderr.write("tty: %s\n" % (error_code_to_text(error.errno)))
        return 1
