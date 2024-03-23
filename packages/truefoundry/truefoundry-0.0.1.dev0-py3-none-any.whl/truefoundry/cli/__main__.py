import os
import sys

import click
from mlfoundry.cli.commands import download
from servicefoundry.cli import create_servicefoundry_cli


@click.group()
def ml():
    """MlFoundry CLI"""


def main():
    # Exit the interpreter by raising SystemExit(status).
    # If the status is omitted or None, it defaults to zero (i.e., success).
    # If the status is an integer, it will be used as the system exit status.
    # If it is another kind of object, it will be printed and the system exit status will be one (i.e., failure).
    ml.add_command(download)
    cli = create_servicefoundry_cli()
    cli.add_command(ml)
    sys.exit(cli())


if __name__ == "__main__":
    main()
