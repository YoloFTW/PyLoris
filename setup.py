from setuptools import setup, find_packages

import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.2'
DESCRIPTION = 'Test websites for slow loris'
LONG_DESCRIPTION = long_description

# Setting up
setup(
    name="PyLoris",
    version=VERSION,
    author="YoloFTW",
    description=DESCRIPTION,
    url='https://github.com/YoloFTW/PyLoris',
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'slow loris', 'test', 'loris', 'slow lorris'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)