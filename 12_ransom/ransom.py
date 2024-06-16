#!/usr/bin/env python3
"""
Author : "e.j. (they/them)" <git@ejs.sh>
Date   : 2024-02-10
Purpose: Randomly capitalizing text
"""

import argparse
import os
import random

from typing import List


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Ransom Note",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument(
        "-s",
        "--seed",
        help="Rondom seed",
        metavar="seed",
        type=int,
        default=None,
    )

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


def choose(ch: str) -> str:
    """Randomly make letters upper or lowercase"""

    return ch.upper() if random.choice([0, 1]) else ch.lower()


def test_choose():
    st = random.getstate()
    random.seed(1)
    assert choose("a") == "a"
    assert choose("b") == "b"
    assert choose("c") == "c"
    assert choose("d") == "d"
    random.setstate(st)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    ransom: List[str] = []
    for ch in args.text:
        ransom.append(choose(ch))

    print("".join(ransom))


# --------------------------------------------------
if __name__ == "__main__":
    main()
