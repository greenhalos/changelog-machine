import argparse
from src.entryGenerator import generateEntry
from src.changelogGenerator import generateChangelog

parser = argparse.ArgumentParser(description='The machine to generate changelogs.')
parser.add_argument('entry', help='To create an entry.', action='store_true')
parser.add_argument('changelog', help='To generate or append the changelog.', action='store_true')

args, action = parser.parse_known_args()

if len(action) == 0:
    parser.print_help()
elif action[0] == 'entry':
    generateEntry()
elif action[0] == 'changelog':
    generateChangelog()
else:
    parser.print_help()
