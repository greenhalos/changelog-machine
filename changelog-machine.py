import argparse
import sys
from src.entryGenerator import generate_entry
from src.changelogGenerator import generate_changelog

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="The machine to generate changelogs.")
    parser.add_argument("entry", help="To create an entry.", action="store_true")
    parser.add_argument(
        "changelog", help="To generate or append the changelog.", action="store_true"
    )

    arguments = sys.argv

    if len(arguments) < 2:
        parser.print_help()
    elif arguments[1] == "entry":
        generate_entry()
    elif arguments[1] == "changelog":
        generate_changelog()
    else:
        args = parser.parse_known_args()
