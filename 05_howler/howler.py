#!/usr/bin/env python3
"""
Author : "e.j. (they/them)" <git@ejs.sh>
Date   : 2024-02-04
Purpose: Working with files and STDOUT
"""

import argparse
import os
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("text", metavar="text", type=str, help="Input text or filename")

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output filename",
        metavar="str",
        type=str,
        default="",
    )

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Howler."""

    args = get_args()
    out_fh = open(args.outfile, "wt") if args.outfile else sys.stdout
    out_fh.write(args.text.upper() + "\n")
    out_fh.close()


# --------------------------------------------------
if __name__ == "__main__":
    main()
