import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="changelog-machine",
    version="0.7.0",
    author="Ben Antony",
    author_email="antony@greenhalos.lu",
    description="A tool to generate changelogs integrated in a pull/merge request workflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/greenhalos/changelog-machine",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
