import sys
from glxshell.lib.argparse import ArgumentParser


parser_unalias = ArgumentParser(
    name="unalias - remove alias definitions",
    description="The unalias utility shall remove the definition for each alias name specified.",
    synopsis=["unalias alias-name..."],
    exit_status={
        "0": "Successful completion.",
        ">0": "One of the alias-name operands specified did not represent a valid alias definition, or an "
              "error occurred."
    },
)

parser_unalias.add_argument(
    "-a",
    dest="a",
    action="store_true",
    help="Remove all alias definitions from the current shell execution environment.",
)

parser_unalias.add_argument(
    "alias-name",
    dest="alias_name",
    nargs="*",
    type=str,
    help="The name of an alias to be removed.",
)


def glxsh_unalias(a=None, alias_name=None, shell=None):
    """
    The unalias utility shall remove the definition for each alias name specified. See Alias Substitution.
    The aliases shall be removed from the current shell execution environment; see Shell Execution Environment.

    :param string: every argument after alias cmg as a single string
    :type string: str
    """
    exit_code = 0
    try:
        if a:
            shell.alias = {}
        else:
            for alias in alias_name:
                if alias in shell.alias:
                    del shell.alias[alias]
                else:
                    exit_code += 1
        return exit_code

    except (Exception, BaseException) as error:  # pragma: no cover
        sys.stderr.write("alias: %s\n" % error)
        return 1
