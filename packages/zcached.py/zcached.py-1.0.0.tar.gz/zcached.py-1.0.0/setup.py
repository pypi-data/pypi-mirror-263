from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "readme.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

VERSION = "1.0.0"
DESCRIPTION = "A lightweight client-side library for zcached, written in Python."

setup(
    name="zcached.py",
    version=VERSION,
    author="xXenvy",
    author_email="<xpimpek01@gmail.com>",
    description=DESCRIPTION,
    license="MIT",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/xxenvy/zcached.py",
    project_urls={
        "Issue tracker": "https://github.com/xxenvy/zcached.py/issues",
    },
    python_requires=">=3.8.0",
    packages=find_packages(),
    install_requires=requirements,
    keywords=[
        "python",
        "redis",
        "redisclient",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 5 - Production/Stable",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Typing :: Typed",
    ],
)
