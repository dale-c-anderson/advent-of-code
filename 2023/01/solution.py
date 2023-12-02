#!/usr/bin/env python3
"""
AdventOfCode.com 2023, Day 01
"""

__author__ = "Dale Anderson"

import argparse
import logging
import sys


def main(data0):

    data0 = data0.splitlines()

    if args.part1 or not args.part2:
        part1_answer = part1(data0)
        print(f'Part 1: {part1_answer}')

    if args.part2 or not args.part1:
        part2_answer = part2(data0)
        print(f'Part 2: {part2_answer}')


def part1(data):

# example data:
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

    running_total = 0
    for line in data:
        # strip non-numerics
        numbers_only = ''.join([i for i in line if i.isdigit()])
        first_digit = numbers_only[0]
        last_digit = numbers_only[-1]
        # glue numbers together into an integer
        two_digit_number = int(first_digit + last_digit)
        running_total += two_digit_number

    return running_total



def part2(data):
    return 0


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?')
    parser.add_argument('-1', '-p1', '--part1', action='store_true', help='Run (only) part 1')
    parser.add_argument('-2', '-p2', '--part2', action='store_true', help='Run (only) part 2')
    parser.add_argument("-v", "--verbose", action="count", default=0, help="Verbosity (-v, -vv, etc)")
    args = parser.parse_args()

    # Accept input from a named file, a pipe, or the default location
    if args.filename:
        data = open(args.filename).read()
    elif not sys.stdin.isatty():
        data = sys.stdin.read()
    else:
        data = open("./input").read()

    # Support verbosity level
    levels = [
        logging.WARNING,
        logging.INFO,
        logging.DEBUG,
    ]
    level = levels[min(args.verbose, len(levels) - 1)]

    # A named logger lets us add more handlers if/when needed.
    log = logging.getLogger("foo")

    # Set the minimum threshold needed by any handler, then override desired levels for each handler.
    # If this is set to "CRITICAL", for instance, nothing will ever appear in any log handler.
    log.setLevel(logging.DEBUG)

    # Set up handler for terminal logging
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setLevel(level)  # Let terminal log level be controlled by args
    default_log_format = '%(levelname)s %(funcName)s(): %(message)s'
    console_handler.setFormatter(logging.Formatter(default_log_format))
    log.addHandler(console_handler)

    main(data)
