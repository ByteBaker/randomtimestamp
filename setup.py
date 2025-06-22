import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="randomtimestamp",
    version="2.3",
    description="Generate random time stamps",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ByteBaker/randomtimestamp",
    author="ByteBaker",
    author_email="42913098+ByteBaker@users.noreply.github.com",
    license="GPL v3.0",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.13",
        "Development Status :: 5 - Production/Stable",
    ],
    packages=["randomtimestamp"],
    include_package_data=True,
    license_files=[],
    install_requires=[

    ],
    entry_points={
        "console_scripts": [
            "randomtimestamp=randomtimestamp.__main__:main",
        ]
    },
)
