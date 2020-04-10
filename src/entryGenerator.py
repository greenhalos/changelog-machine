import argparse
import re
import os


def generate_entry():
    parser = argparse.ArgumentParser(description="Create a changelog entry.")
    parser.add_argument("entry", help="To create an entry.", action="store_true")
    parser.add_argument(
        "-i", "--issue-id", help="The issue id without the #", default=""
    )
    parser.add_argument(
        "-mr", "--merge-request", help="The merge request id", default=""
    )
    parser.add_argument("-a", "--author", help="The author of the change", default="")
    parser.add_argument("-m", "--message", help="The message of the entry", required=True)

    args, unknown = parser.parse_known_args()

    entry = """---
    title: '{}'
    merge_request: {}
    issue: {}
    author: {}
    """.format(
        args.message, args.merge_request, args.issue_id, args.author
    )

    directory = "./changelogs/unreleased"

    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = "{}/{}.yml".format(directory, re.sub("[^0-9a-zA-Z]+", "_", args.message))
    with open(filename, "w") as out:
        out.write(entry)
