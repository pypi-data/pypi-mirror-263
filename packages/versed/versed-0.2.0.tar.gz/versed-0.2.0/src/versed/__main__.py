import urllib.request
import urllib.parse
import os
import argparse
import json
from pprint import pprint


def init():
    if os.path.exists(".versed"):
        print("Versed configuration has already been initialized.")
    else:
        with open(".versed", "w") as f:
            pass
        print("Initialized new Versed configuration file.")


def select_verse(scripture_reference: str):
    url_str = f"https://api.esv.org/v3/passage/text/?q={scripture_reference.replace(' ', '+')}"
    if os.path.exists(".versed"):
        with open(".versed", "r") as f:
            token = f.read()
        headers = {"Authorization": token}
        # encoded_headers = urllib.parse.urlencode(headers).encode('utf-8')
        req = urllib.request.Request(url_str, headers=headers)
        with urllib.request.urlopen(req) as response:
            res = response.read()
        pprint(json.loads(res))
    else:
        print(
            "No Versed configuration found. Please run python -m versed init and put your API token in the .versed configuration file that is created"
        )


def main():
    parser = argparse.ArgumentParser(
        prog="Versed",
        description="'I have stored up your word in my heart, that I might not sin against you.' Psalm 119:11",
    )
    parser.add_argument("-i", "--init", action="store_true")
    parser.add_argument("-s", "--select")
    args = parser.parse_args()

    if args.init:
        init()
    elif args.select:
        select_verse(args.select)


if __name__ == "__main__":
    main()
