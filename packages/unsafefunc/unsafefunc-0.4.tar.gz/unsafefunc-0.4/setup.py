from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='unsafefunc',
    version='0.4',
    packages=find_packages(),
    description='Better not use on main pc. For education purposes only!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='TheDanDev'
)
