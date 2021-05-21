from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="azcam-ascom",
    version="21.0.0",
    description="azcam extension for ASCOM cameras",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Michael Lesser",
    author_email="mlesser@arizona.edu",
    keywords="",
    packages=find_packages(),
    zip_safe=False,
    url="https://mplesser.github.io/azcam/",
    install_requires=["azcam"],
)
