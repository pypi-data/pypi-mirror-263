import setuptools
from pathlib import Path

setuptools.setup(
    name="arkopalpdf",
    version=1.11,
    long_description=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude=["tests", "data"])
    # ignores those 2 folders
)
