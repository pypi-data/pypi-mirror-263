# inspired by: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/uname.html

import os
import sys
from glxshell.lib.argparse import ArgumentParser
from glxshell.lib.utils import error_code_to_text


parser_uname = ArgumentParser(
    name="uname - return system name",
    description="By default, the uname utility shall write the operating system name to standard output. When options "
    "are specified, symbols representing one or more system characteristics shall be written to the "
    "standard output.",
)
parser_uname.add_argument(
    "-a",
    dest="all",
    action="store_true",
    help="Behave as though all of the options -mnrsv were specified.",
)
parser_uname.add_argument(
    "-s",
    dest="sysname",
    action="store_true",
    help="Write the name of the implementation of the operating system.",
)
parser_uname.add_argument(
    "-n",
    dest="nodename",
    action="store_true",
    help="Write the name of this node within an implementation-defined communications network.",
)
parser_uname.add_argument(
    "-r",
    dest="release",
    action="store_true",
    help="Write the current release level of the operating system implementation.",
)
parser_uname.add_argument(
    "-v",
    action="store_true",
    dest="version",
    help="Write the current version level of this release of the operating system implementation.",
)
parser_uname.add_argument(
    "-m",
    dest="machine",
    action="store_true",
    help="Write the name of the hardware type on which the system is running.",
)


def glxsh_uname(all=False, sysname=False, nodename=False, release=False, version=False, machine=False):
    try:
        info = os.uname()

        def gen_lines():
            if all or nodename:
                yield info.nodename

            if all or release:
                yield info.release

            if all or version:
                yield info.version

            if all or machine:
                yield info.machine

        lines = list(gen_lines())
        if all or sysname or (not lines):
            lines.insert(0, info.sysname)

        sys.stdout.write("%s\n" % " ".join(lines))
        return 0

    except (Exception, ArithmeticError) as error:  # pragma: no cover
        sys.stderr.write("uname: %s\n" % (error_code_to_text(error.errno)))
        return 1
