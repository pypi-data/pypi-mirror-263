from glxshell.lib.argparse import ArgumentParser


parser_false = ArgumentParser(
    name="false - return false value",
    synopsis=["false"],
    description="The false utility shall return with a non-zero exit code.",
    exit_status={
        "1": "",
    }
)


def glxsh_false():
    return 1
