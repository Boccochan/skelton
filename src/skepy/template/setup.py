import io
import re
import glob
import os

from setuptools import find_packages
from setuptools import setup

version_file_path = os.path.join('src', '${PKG_NAME}', '__init__.py')

with io.open(version_file_path, "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

template_files = []
for file_name in glob.glob(os.path.join('src', '${PKG_NAME}', 'data', '**'), recursive=True):
    template_files.append(file_name.split(os.path.sep, 2)[-1])

setup(
    name="${PKG_NAME}",
    version=version,
    install_requires=[],
    extras_require={
        "test": [
            "flake8",
            "pytest",
        ],
    },
    packages=["${PKG_NAME}"],
    package_dir={"${PKG_NAME}": "src/${PKG_NAME}"},
    package_data={"${PKG_NAME}": template_files},
    python_requires="~=3.8",
    entry_points={"console_scripts": ["${PKG_NAME} = src.${PKG_NAME}.cli:main"]},
)