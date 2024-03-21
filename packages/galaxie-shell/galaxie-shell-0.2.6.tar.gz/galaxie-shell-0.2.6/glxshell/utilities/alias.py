import sys
from glxshell.lib.argparse import ArgumentParser
from glxshell.lib.utils import error_code_to_text
from glxshell.lib.utils import quoted_split

parser_alias = ArgumentParser(
    name="alias - define or display aliases",
    description="The alias utility shall create or redefine alias definitions or write the values of existing alias "
                "definitions to standard output. An alias definition provides a string value that shall replace a "
                "command name when it is encountered",
    synopsis=["alias [alias-name[=string]...]"],
    exit_status={
        "0": "Successful completion.",
        ">0": "One of the name operands specified did not have an alias definition, or an error occurred."
    },
)
parser_alias.add_argument(
    "alias-name",
    nargs="*",
    type=str,
    help="Write the alias definition to standard output.",
)

parser_alias.add_argument(
    "alias-name=string",
    nargs="*",
    help="Assign the value of string to the alias alias-name.",
)


def glxsh_alias(**kwargs):
    """
    The alias utility shall create or redefine alias definitions or write the values of existing alias
    definitions to standard output. An alias definition provides a string value that shall replace a command
    name when it is encountered;

    :param string: every argument after alias cmg as a single string
    :type string: str
    """
    shell = kwargs.get("shell", None)
    string = kwargs.get("string", None)

    exit_code = 0
    if string is None:
        if shell:
            for key, value in shell.alias.items():
                sys.stdout.write("%s='%s'\n" % (key, value))
            return 0
        else:
            return 1
    try:
        split_line = quoted_split(string)
        if split_line:
            for alias_name in split_line:
                if "=" in alias_name:
                    spited_value = alias_name.split("=")
                    shell.alias[spited_value[0]] = str(spited_value[1].strip('\"').strip('\''))

                elif alias_name in shell.alias:
                    sys.stdout.write("%s='%s'\n" % (alias_name, shell.alias[alias_name]))

            return exit_code
        else:
            for key, value in shell.alias.items():
                sys.stdout.write("%s='%s'\n" % (key, value))
            return 0
    except OSError as error:  # pragma: no cover
        sys.stderr.write("alias: %s\n" % (error_code_to_text(error.errno)))
        return 1
