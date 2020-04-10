import argparse


def generateChangelog():
    parser = argparse.ArgumentParser(description='Create a changelog entry.')
    parser.add_argument('changelog', help='To generate or append the changelog.', action='store_true')
    parser.add_argument('releaseVersion', help='The version of the release')

    args, unknown = parser.parse_known_args()

    print("Hello I will generate your changelog")
