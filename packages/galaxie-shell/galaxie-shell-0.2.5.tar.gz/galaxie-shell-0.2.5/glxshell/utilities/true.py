from glxshell.lib.argparse import ArgumentParser


parser_true = ArgumentParser(
    name="true - return true value",
    synopsis=["true"],
    description="The true utility shall return with exit code zero.",
    exit_status={
        "0": "",
    }
)


def glxsh_true():
    return 0
