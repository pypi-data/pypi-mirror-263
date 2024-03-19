# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md") as rdm:
    long_description = rdm.read()

with open("requirements.txt") as req:
    install_requires = req.read()

setup(
    name="j2yaml",
    version="0.1.1",
    description="Jinja2-templates inside YAML-files.",
    license="GPLv3",
    author="tombayo",
    author_email="pypi@tombayo.com",
    url="https://github.com/tombayo/j2yaml",
    packages=["j2yaml"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=install_requires,
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"]
    },
    python_requires=">=3.8"
)
