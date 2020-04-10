#!/bin/bash

rm -rf dist Changelog_machine.egg-info
echo "Setting current version"
bump2version --current-version "$(python3 setup.py --version)" minor setup.py
echo "Current version: $(python3 setup.py --version)"
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository testpypi dist/* 
