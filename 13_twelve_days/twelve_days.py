#!/usr/bin/env python3
"""
Author : "e.j. (they/them)" <git@ejs.sh>
Date   : 2024-02-10
Purpose: Twelve Days of Christmas
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Twelve Days of Christmas",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-n",
        "--num",
        help="Number of days to sing",
        metavar="days",
        type=int,
        default=12,
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Outfile",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
    )

    args = parser.parse_args()

    if args.num not in range(1, 13):
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


def verse(day):
    """Create a verse"""

    _ordinal = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth",
    ]

    _verses = [
        "A partridge in a pear tree.",
        "Two turtle doves,",
        "Three French hens,",
        "Four calling birds,",
        "Five gold rings,",
        "Six geese a laying,",
        "Seven swans a swimming,",
        "Eight maids a milking,",
        "Nine ladies dancing,",
        "Ten lords a leaping,",
        "Eleven pipers piping,",
        "Twelve drummers drumming,",
    ]

    _lines = [
        f"On the {_ordinal[day - 1]} day of Christmas,",
        "My true love gave to me,",
    ]
    _lines.extend(reversed(_verses[:day]))

    if day > 1:
        _lines[-1] = "And " + _lines[-1].lower()

    return "\n".join(_lines)


def test_verse():
    """Test verse"""
    assert verse(1) == "\n".join(
        [
            "On the first day of Christmas,",
            "My true love gave to me,",
            "A partridge in a pear tree.",
        ]
    )
    assert verse(2) == "\n".join(
        [
            "On the second day of Christmas,",
            "My true love gave to me,",
            "Two turtle doves,",
            "And a partridge in a pear tree.",
        ]
    )


# --------------------------------------------------
def main():
    """Twelve Days of Christmas"""

    args = get_args()
    verses = map(verse, range(1, args.num + 1))
    print("\n\n".join(verses), file=args.outfile)


# --------------------------------------------------
if __name__ == "__main__":
    main()
