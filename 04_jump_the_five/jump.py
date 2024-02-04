#!/usr/bin/env python3
"""
Author : "e.j. (they/them)" <git@ejs.sh>
Date   : 2024-02-03
Purpose: Jump the Five
"""

import argparse

from typing import Dict


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="str", help="Input text")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    jumper: Dict = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5",
    }

    args = get_args()

    for ch in args.text:
        print(jumper.get(ch, ch), end="")
    print()


# --------------------------------------------------
if __name__ == "__main__":
    main()
