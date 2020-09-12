#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages
from os.path import dirname, join

with open(join(dirname("."), "VERSION"), "rb") as f:
    version = f.read().decode("ascii").strip()

setup(
    name="{message_board}",
    version=version,
    python_requires=">=3.7.0",
    author="Dung Ho",
    author_email="dung.ho@edu.turkuamk.fi",
    long_description="""
    This is a simple message board web application with two services:
    - createMessage
    - listMessages
    """,
    packages=find_packages(),
    py_modules=["{message_board}"],
    include_package_data=True,
    zip_safe=False,
)
