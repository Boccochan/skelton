import io
import os
import re
import glob

from setuptools import find_packages
from setuptools import setup

version_file_path = os.path.join('src', 'skepy', '__init__.py')
with io.open("src/skepy/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

template_files = []
for file_name in glob.glob(os.path.join('src', 'skepy', 'template', '**'), recursive=True):
    template_files.append(file_name.split(os.path.sep, 2)[-1])

setup(
    name="skepy",
    version=version,
    author="Yasuhiro Ito",
    author_email="boccochan@gmail.com",
    maintainer="Yasuhiro Ito",
    maintainer_email="boccochan@gmail.com",
    description="Calculate time of python code.",
    install_requires=[
        "click",
    ],
    extras_require={
        "test": [
            "pytest",
        ],
    },
    packages=['skepy'],
    package_dir={"skepy": "src/skepy"},
    package_data={'skepy': template_files},
    python_requires="~=3.8",
    entry_points={"console_scripts": ["skepy = src.skepy.cli:main"]},
)
