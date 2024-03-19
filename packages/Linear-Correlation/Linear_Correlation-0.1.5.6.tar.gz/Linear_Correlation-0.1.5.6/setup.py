from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1.5.6'
DESCRIPTION = 'Linear Correlation Analysis and Data Preprocessing Tools'

# Setting up
setup(
    name="Linear_Correlation",
    version=VERSION,
    author="chingDev.Official (Prince Carl Ajoc)",
    author_email="chingace471@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    keywords=['linear correlation', 'correlation analysis', 'numerical analysis', 'data preprocessing', 'data science', 'pandas'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)