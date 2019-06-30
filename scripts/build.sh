#! /usr/bin/env bash

pip3 install -r requirements.txt
pyinstaller -y --onefile --name changelog-machine main.py
