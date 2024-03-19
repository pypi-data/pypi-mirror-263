from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.2.5'
DESCRIPTION = 'Python class for imputing missing values in data columns using various imputation strategies based on data types.'

# Setting up
setup(
    name="Missing_Value",
    version=VERSION,
    author="chingDev.Official (Prince Carl Ajoc)",
    author_email="chingace471@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'numpy', "statistics"],
    keywords=['missing data', 'imputation', 'data preprocessing', 'data cleaning', 'data analysis', 'pandas', 'numpy', 'statistics'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)