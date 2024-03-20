from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.1'
DESCRIPTION = 'A Python package for fetching and processing data from a Census API'

# Setting up
setup(
    name="censusWrapper",
    version=VERSION,
    author="lennon0926",
    author_email="<onnelle.lugo@upr.edu>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['requests', 'pandas'],
    keywords=['python', 'api', 'request', 'census', 'data', 'pandas', 'wrapper'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)