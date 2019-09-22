import io
import re

from setuptools import find_packages
from setuptools import setup

with io.open("src/skepy/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="skepy",
    version=version,
    author="Yasuhiro Ito",
    author_email="boccochan@gmail.com",
    maintainer="Yasuhiro Ito",
    maintainer_email="boccochan@gmail.com",
    description="Calculate time of python code.",
    packages=find_packages("src"),
    install_requires=[
        "click",
    ],
    extras_require={
        "test": [
            "pytest",
        ],
    },
    package_dir={"": "src"},
    python_requires="~=3.7",
    entry_points={"console_scripts": ["skepy = skepy.cli:main"]},
)
