#!/usr/bin/env python3
"""
Author : "e.j. (they/them)" <git@ejs.sh>
Date   : 2024-02-04
Purpose: Find and replace
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Apples and bananas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Input text or file")

    parser.add_argument(
        "-v",
        "--vowel",
        help="The vowel to substitute",
        metavar="vowel",
        type=str,
        default="a",
        choices=list("aeiou"),
    )

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Apples and bananas"""

    args = get_args()
    text = args.text
    vowel = args.vowel
    new_text = []

    for ch in text:
        if ch in "aeiou":
            new_text.append(vowel)
        elif ch in "AEIOU":
            new_text.append(vowel.upper())
        else:
            new_text.append(ch)

    print("".join(new_text))


# --------------------------------------------------
if __name__ == "__main__":
    main()
