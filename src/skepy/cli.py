import os
import sys
import json
import click
from typing import Optional
from src.skepy import skeleton


@click.command()
@click.argument("package", required=False)
def main(package):
    """ Create a new python package template """
    proj = skeleton.Project(package)

    return proj.create_skeleton()


if __name__ == "__main__":
    sys.exit(main())