# SPDX-FileCopyrightText: 2024 UL Research Institutes
# SPDX-License-Identifier: MIT

from setuptools import find_packages, setup

# injected version
__version__ = "0.12.0"

# markdown readme
long_description = open("README.md").read()

# read requirements from requirements.in
install_requires = open("requirements.in").read().splitlines()

setup(
    name="badgie",
    version=__version__,
    author="Digital Safety Research Institute",
    author_email="contact@dsri.org",
    description="Add all the badges with Badgie!",
    license="MIT",
    url="https://gitlab.com/buildgarden/tools/badgie",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    package_data={"badgie": ["py.typed"]},
    entry_points={
        "console_scripts": [
            "badgie = badgie.cli:main",
        ],
    },
    install_requires=install_requires,
    python_requires=">=3.9",
    keywords=["badge", "template", "markdown"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Utilities",
    ],
)
