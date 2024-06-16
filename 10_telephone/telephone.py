#!/usr/bin/env python3
"""
Author : "e.j. (they/them)" <git@ejs.sh>
Date   : 2024-02-10
Purpose: Telephone, randomly mutating strings
"""

import argparse
import os
import random
import string

from typing import List


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Telephone", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument(
        "-s", "--seed", help="Random seed", metavar="seed", type=int, default=None
    )

    parser.add_argument(
        "-m",
        "--mutations",
        help="Percent mutations",
        metavar="mutations",
        type=float,
        default=0.1,
    )

    args = parser.parse_args()

    # ensure that mutations are within range
    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')
    # if given a path, open it
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Telephone: Randonly mutating string."""

    args = get_args()
    random.seed(args.seed)

    num_mutations: int = round(len(args.text) * args.mutations)
    # use the string module to concatenate sorted letters and punctuation
    alpha: str = "".join(sorted(string.ascii_letters + string.punctuation))
    new_text: List[str] = list(args.text)

    for i in random.sample(range(len(args.text)), num_mutations):
        new_text[i] = random.choice(alpha.replace(new_text[i], ""))

    # join the new_text list
    nt: str = "".join(new_text)
    print(f'You said: "{args.text}"')
    print(f'I heard : "{nt}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
