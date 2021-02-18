#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Kenzie Assignment: Valid Brackets
"""

# Your name, plus anyone who helped you with this assignment.
# Give credit where credit is due.
__author__ = "???"

import sys


def is_valid(expr):
    """
    Returns True if the brackets within the given expression
    are opened and closed properly, or False if they are not.
    """
    # your code here
    pass


def main(args):
    """Call `is_valid()` for the expression passed in."""
    if len(args) != 1:
        print('usage: python brackets.py expression')
        sys.exit(1)

    expr = sys.argv[1]

    print(is_valid(expr))


if __name__ == '__main__':
    main(sys.argv[1:])
