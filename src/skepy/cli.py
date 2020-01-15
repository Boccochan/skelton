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
    proj.copy_template()
    proj.apply_pkg_name_to_src_dir()
    proj.apply_pkg_name_to_files()


if __name__ == "__main__":
    main()