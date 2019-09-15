from os import environ

from setuptools import setup, find_packages

version = environ.get("CURRENT_VERSION", "SNAPSHOT")

setup(
    name="python-template",
    version=version,
    author="Samuel Pedro",
    description="Python Template",
    include_package_data=True,
    install_requires=[],
    data_files=[],
    packages=find_packages(),
)
