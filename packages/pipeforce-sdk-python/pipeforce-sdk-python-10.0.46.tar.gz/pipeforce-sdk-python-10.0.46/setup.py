import os

import setuptools

build_number = os.environ["GITHUB_RUN_NUMBER"]

with open("README.MD", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pipeforce-sdk-python",  # This is the name of the package
    version="10.0." + str(build_number),  # The initial release version
    author="LOGABIT GmbH",  # Full name of the author
    description="Python SDK for PIPEFORCE",
    long_description=long_description,  # Long description read from the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),  # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],  # Information to filter the project on PyPi website
    python_requires='>=3.9',  # Minimum version requirement of the package
    py_modules=["pipeforce_sdk"],  # Name of the python package
    package_dir={'': 'pipeforce-sdk-python/src'},  # Directory of the source code of the package
    install_requires=[]  # Install other dependencies if any
)
