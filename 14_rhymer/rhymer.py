#!/usr/bin/env python3
"""
Author : "e.j. (they/them)" <git@ejs.sh>
Date   : 2024-02-11
Purpose: Using regular expressions to create rhyming words
"""

import argparse
import re
import string as s

from typing import Tuple


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("word", metavar="word", help="A word to rhyme")

    return parser.parse_args()


def stemmer(w: str) -> Tuple:
    """Return leading consonants (if any), and 'stem' of word"""

    w = w.lower()
    _v = "aeiou"
    _c = "".join([c for c in s.ascii_lowercase if c not in _v])
    _p = "([" + _c + "]+)?" "([" + _v + "])" "(.*)"
    _m = re.match(_p, w)
    if _m:
        p1 = _m.group(1) or ""
        p2 = _m.group(2) or ""
        p3 = _m.group(3) or ""
        return (p1, p2 + p3)
    else:
        return (w, "")


def test_stemmer():
    """Test stemmer"""
    assert stemmer("") == ("", "")
    assert stemmer("cake") == ("c", "ake")
    assert stemmer("chair") == ("ch", "air")
    assert stemmer("APPLE") == ("", "apple")
    assert stemmer("RDNZL") == ("rdnzl", "")
    assert stemmer("123") == ("123", "")


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    prefixes = (
        list("bcdfghjklmnpqrstvwxyz")
        + (
            "bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp "
            "st sw th tr tw thw wh wr sch scr shr sph spl spr squ str thr"
        ).split()
    )

    st, rest = stemmer(args.word)
    if rest:
        print("\n".join(sorted([p + rest for p in prefixes if p != st])))
    else:
        print(f'Cannot rhyme "{args.word}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
