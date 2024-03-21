from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="boomtils",
    version="1.0.69",
    author="iusebako",
    author_email="leaf5ter@tuta.io",
    description="The most useless package ever created.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/real-kwellercat/boomtils.py",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)