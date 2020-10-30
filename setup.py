#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for anyblok-background-tasks"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
import os

from setuptools import find_packages, setup

version: str = "0.1.0"
here: str = os.path.abspath(os.path.dirname(__file__))

with open(
    os.path.join(here, "README.rst"), "r", encoding="utf-8"
) as readme_file:
    readme = readme_file.read()

with open(
    os.path.join(here, "CHANGELOG.rst"), "r", encoding="utf-8"
) as changelog_file:
    changelog = changelog_file.read()

requirements: "List[str]" = [
    "sqlalchemy",
    "anyblok",
]

test_requirements: "List[str]" = [
    # TODO: put package test requirements here
]

setup(
    name="anyblok_background_tasks",
    version=version,
    description="Abstractions and tools to manage background tasks",
    long_description=readme + "\n\n" + changelog,
    author="Pierre Verkest",
    author_email="pierreverkest84@gmail.com",
    url="https://github.com/petrus-v/anyblok-background-tasks",
    packages=find_packages(),
    entry_points={
        "bloks": ["core_task=anyblok_background_tasks.core_task:Core_task"]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords="anyblok-background-tasks",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    test_suite="tests",
    tests_require=test_requirements,
)
