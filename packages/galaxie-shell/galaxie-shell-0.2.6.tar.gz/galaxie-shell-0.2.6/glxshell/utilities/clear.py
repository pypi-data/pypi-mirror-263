import sys

from glxshell.lib.argparse import ArgumentParser


parser_clear = ArgumentParser(
    name="clear",
    description="Clear screen",
)


def glxsh_clear():
    """
    Internal function it clear the screen
    """
    try:
        sys.stdout.write("\x1b[2J\x1b[H")
        return 0
    except (Exception, ArithmeticError) as error:  # pragma: no cover
        sys.stderr.write("clear: %s\n" % error)
        return 1
