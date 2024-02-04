#!/usr/bin/env python3
"""
Author : "e.j. (they/them)" <git@ejs.sh>
Date   : 2024-02-03
Purpose: Crow's Nest -- choose the correct article.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("word", metavar="word", help="A word")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """
    Given a positional input, prints the phrase:
        "Ahoy, Captain, (a|an) {word} off the larboard bow!"
    """

    args = get_args()
    word = args.word
    article = "an" if word[0].lower() in "aeiou" else "a"

    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")


# --------------------------------------------------
if __name__ == "__main__":
    main()
