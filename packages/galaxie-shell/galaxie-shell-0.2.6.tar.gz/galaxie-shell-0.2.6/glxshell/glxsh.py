#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from glxshell.lib.argparse import ArgumentParser
from glxshell.lib.path import isfile
from glxshell.lib.ush import GLXUsh

# https://fallout.fandom.com/wiki/Pip-OS_v7.1.0.8
# https://fallout.fandom.com/wiki/Terminal
# https://fallout.fandom.com/wiki/Unified_Operating_System
# https://fallout.fandom.com/wiki/RETROS_BIOS
# https://fallout.fandom.com/wiki/MF_Boot_Agent

parser_glxsh = ArgumentParser(
    prog="glxsh",
    add_help=True,
)
parser_glxsh.add_argument(
    "command",
    nargs="?",
    help="optional commands or file to run, if no commands given, enter an interactive shell",
)
parser_glxsh.add_argument(
    "command_args",
    nargs="...",
    help="if commands is not a file use optional arguments for commands",
)


def main():
    if len(sys.argv) > 1:

        args = parser_glxsh.parse_args(sys.argv[1:])
        if args.help:
            parser_glxsh.print_help()
            return 0

        if isfile(args.command):
            try:
                with open(args.command) as rcFile:
                    for line in rcFile.readlines():
                        line = line.rstrip()
                        if len(line) > 0 and line[0] != "#":
                            exit_code = GLXUsh().onecmdhooks("%s" % line)
            except IOError:
                exit_code = 1
            else:
                return exit_code

        else:
            return GLXUsh().onecmdhooks("%s %s" % (args.command, " ".join(args.command_args)))

    else:
        return GLXUsh().cmdloop()


if __name__ == "__main__":
    sys.exit(main())
