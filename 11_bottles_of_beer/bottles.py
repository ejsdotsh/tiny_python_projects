#!/usr/bin/env python3
"""
Author : "e.j. (they/them)" <git@ejs.sh>
Date   : 2024-02-10
Purpose: Writing and testing functions
"""

import argparse

from typing import List


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Bottles of beer song",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n", "--num", help="How many bottles", metavar="number", type=int, default=10
    )

    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


def verse(bottle: int) -> str:
    """'Sing' a verse."""

    _next_bottle: int = bottle - 1
    _s1: str = "" if bottle == 1 else "s"
    _s2: str = "" if _next_bottle == 1 else "s"
    _num_next = "No more" if _next_bottle == 0 else _next_bottle
    return "\n".join(
        [
            f"{bottle} bottle{_s1} of beer on the wall,",
            f"{bottle} bottle{_s1} of beer,",
            "Take one down, pass it around,",
            f"{_num_next} bottle{_s2} of beer on the wall!",
        ]
    )


def test_verse() -> None:
    """Test verse."""

    last_verse = verse(1)
    assert last_verse == "\n".join(
        [
            "1 bottle of beer on the wall,",
            "1 bottle of beer,",
            "Take one down, pass it around,",
            "No more bottles of beer on the wall!",
        ]
    )

    two_bottles = verse(2)
    assert two_bottles == "\n".join(
        [
            "2 bottles of beer on the wall,",
            "2 bottles of beer,",
            "Take one down, pass it around,",
            "1 bottle of beer on the wall!",
        ]
    )


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    verses: List[str] = [verse(v) for v in range(args.num, 0, -1)]
    print("\n\n".join(verses))


# --------------------------------------------------
if __name__ == "__main__":
    main()
