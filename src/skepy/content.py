
def SETUP_PY(pkg_name: str) -> str:
    setup = f'''
import io
import re

from setuptools import find_packages
from setuptools import setup

with io.open("src/{pkg_name}/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="{pkg_name}",
    version=version,
    packages=find_packages("src"),
    install_requires=[],
    extras_require={{
        "test": [
            "pytest",
        ],
    }},
    package_dir={{"": "src"}},
    python_requires="~=3.7",
    entry_points={{"console_scripts": ["{pkg_name} = {pkg_name}.cli:main"]}},
)
'''
    return setup


def INIT_FILE() -> str:
    init = '''
__version__ = "0.0.0"

'''
    return init


def CLI() -> str:
    cli = '''
def main():
    print("Hello World")


if __name__ == "__main__":
    main()
'''
    return cli


def GITIGNORE() -> str:
    gitignore = '''
__pycache__
*egg-info
dist
build
'''
    return gitignore