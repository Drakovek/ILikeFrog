#~/usr/bin/env python3

import setuptools

console_scripts = ["ilikefrog = i_like_frog.main.ilikefrog:main"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ILikeFrog",
    version="0.0.2",
    author="Drakovek",
    author_email="DrakovekMail@gmail.com",
    description="Utility for converting to and from Frog-Talk",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Drakovek/ILikeFrog",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.0",
    entry_points={"console_scripts": console_scripts}
)
