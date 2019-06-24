import argparse
from entryGenerator import generateEntry

parser = argparse.ArgumentParser(description='The machine to generate changelogs.')
parser.add_argument('entry', help='To create an entry.', action='store_true')
parser.add_argument('changelog-generation', help='To generate the changelog.', action='store_true')

args, action = parser.parse_known_args()

if len(action) == 0:
    parser.print_help()
elif action[0] == 'entry':
    generateEntry()
elif action[0] == 'changelog-generation':
    print('I would do an changelog-generation')
else:
    parser.print_help()
