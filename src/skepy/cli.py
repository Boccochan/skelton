import os
import sys
import json
import click
from typing import Optional
from skepy.content import SETUP_PY, INIT_FILE, CLI, GITIGNORE


def create_package_template(dir_path: str, package: Optional[str]=None) -> None:
    if package:
        os.makedirs(package, exist_ok=True)
        os.chdir(package)
    else:
        package = os.path.split(dir_path)[-1]

    pkg_src = os.path.join('src', os.getcwd().split(os.sep)[-1])

    os.makedirs(pkg_src, exist_ok=True)

    with open(os.path.join(pkg_src, '__init__.py'), 'w') as f:
        f.write(INIT_FILE())

    with open(os.path.join(pkg_src, 'cli.py'), 'w') as f:
        f.write(CLI())

    os.makedirs('tests', exist_ok=True)

    with open('setup.py', 'w') as f:
        f.write(SETUP_PY(package))

    with open('.gitignore', 'w') as f:
        f.write(GITIGNORE())


@click.command()
@click.argument("package", required=False)
def main(package):
    """ Create a new python package template """
    dir_path = os.path.dirname(sys.modules[__name__].__file__)

    create_package_template(dir_path, package)


if __name__ == "__main__":
    main()