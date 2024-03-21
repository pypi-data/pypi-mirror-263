# inspired by: https://pubs.opengroup.org/onlinepubs/9699919799/utilities/env.html

import sys
import subprocess
from glxshell.lib.argparse import ArgumentParser


parser_env = ArgumentParser(
    name="env - set the environment for command invocation",
    description="The env utility shall obtain the current environment, modify it according to its arguments, "
    "then invoke the utility named by the utility operand with the modified environment.",
)
parser_env.add_argument(
    "-i",
    dest="invoke",
    action="store_true",
    help="Invoke utility with exactly the environment specified by the arguments; the inherited environment shall "
    "be ignored completely.",
)
parser_env.add_argument(
    "name",
    nargs="?",
    dest="name",
    help="Arguments of the form name= value shall modify the execution environment, and shall be placed into the "
    "inherited environment before the utility is invoked.",
)
parser_env.add_argument(
    "utility",
    nargs="?",
    dest="utility",
    help="The name of the utility to be invoked. If the utility operand names any of the special built-in "
    "utilities in Special Built-In Utilities, the results are undefined.",
)
parser_env.add_argument(
    "argument",
    nargs="?",
    dest="argument",
    help="A string to pass as an argument for the invoked utility.",
)


def glxsh_env(name, utility, argument, shell):

    if shell and hasattr(shell, "environ"):
        if name:
            try:
                func = getattr(shell, "do_" + utility)
                return func(argument)
            except AttributeError:
                try:
                    pr = subprocess.run(utility, argument, env=shell.environ)
                    return pr.returncode
                except (Exception, BaseException):
                    return shell.default(utility)
        else:
            for name, value in shell.environ.items():
                sys.stdout.write("%s=%s\n" % (name, value))
            return 0
