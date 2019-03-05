#!/usr/bin/env python3
"""
Multiplication table.
"""
import sys


def mult(number):
    """
    Mult.
    """
    align = len(str(10 * number))
    for i in range(11):
        print(f"{i:>2} * {number} = {i * number:>{align}}")


def usage():
    """
    Usage.
    """
    print(f"Usage: {sys.argv[0]} <number>")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        exit()

    NUM = int(sys.argv[1])
    mult(NUM)
