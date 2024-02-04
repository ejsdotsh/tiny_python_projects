#!/usr/bin/env python3
"""
Author : "e.j. (they/them)" <git@ejs.sh>
Date   : 2024-02-03
Purpose: Going on a picnic: Working with lists
"""

import argparse

from typing import List


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Picnic game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("-s", "--sorted", help="Sort the items", action="store_true")
    parser.add_argument("str", metavar="str", help="Item(s) to bring", nargs="+")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """
    Prints what we are bringing to the picnic.
    """

    args = get_args()
    items: List[str] = args.str
    if args.sorted:
        items.sort(key=str.lower)

    num_items: int = len(items)
    if num_items == 1:
        bringing = items[0]
    elif len(items) == 2:
        bringing = " and ".join(items)
    else:
        items[-1] = "and " + items[-1]
        bringing = ", ".join(items)

    print(f"You are bringing {bringing}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
