import argparse
import sys
from src.entryGenerator import generateEntry
from src.changelogGenerator import generateChangelog

parser = argparse.ArgumentParser(description='The machine to generate changelogs.')
parser.add_argument('entry', help='To create an entry.', action='store_true')
parser.add_argument('changelog', help='To generate or append the changelog.', action='store_true')

arguments = sys.argv

if len(arguments) == 0:
    parser.print_help()
elif arguments[1] == 'entry':
    generateEntry()
elif arguments[1] == 'changelog':
    generateChangelog()
else:
    args = parser.parse_known_args()
