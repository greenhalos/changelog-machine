#!/bin/bash

echo "### Cleanup ###"
rm -rf dist changelog_machine.egg-info

echo "### Run tests ###"
python3 -m pytest .

bump2version --current-version "$(python3 setup.py --version)" minor setup.py
echo "### New version: $(python3 setup.py --version) ###"

echo "### Building dist ###"
python3 setup.py sdist bdist_wheel

echo "### Uploading ###"
python3 -m twine upload --repository testpypi dist/* 
