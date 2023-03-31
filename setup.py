from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'Comparing RDS parameter group in AWS account'
LONG_DESCRIPTION = 'A package that allows to compare RDS instance and RDS cluster custom parameter group to their default family parameter group.'

# Setting up
setup(
    name="comparerdspg",
    version=VERSION,
    author="Tanmay Varade",
    author_email="<tanmayvarade235@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['json', 'pandas'],
    keywords=['python', 'compare', 'RDS', 'parameter', 'group', 'AWS', 'devops'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: DevOps",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
