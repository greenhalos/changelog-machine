import argparse
import re
import os

def generateChangelog():

    parser = argparse.ArgumentParser(description='Create a changelog entry.')
    parser.add_argument('changelog', help='To generate or append the changelog.', action='store_true')
    parser.add_argument('-r', '--release', help='The version of the release', required = True)

    args, unknown = parser.parse_known_args()

    print("Hello I will generate your changelog")
