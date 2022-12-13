#!/usr/bin/env python3
"""
AdventOfCode.com 2022, Day 13
"""

__author__ = "Dale Anderson"

import argparse
import logging
import sys
import json


def main(data0):
    data0 = data0.split('\n\n')

    if args.part1 or not args.part2:
        part1_answer = part1(data0)
        print(f'Part 1: {part1_answer}')

    if args.part2 or not args.part1:
        part2_answer = part2(data0)
        print(f'Part 2: {part2_answer}')

global level
level = 0
def part1(data):
    corrects = []
    for index, pair in enumerate(data):
        log.debug(f'pair: {index + 1}')
        left = json.loads(pair.split('\n')[0])
        right = json.loads(pair.split('\n')[1])
        if left_side_is_smaller(left, right):
            corrects.append(index + 1)
        log.debug(f'corrects: {corrects}')
        log.debug('')
    return sum(corrects)


def left_side_is_smaller(left, right):
    global level
    level += 1
    indent = ' ' * level
    ret = None  # Default == no determination ... keep checking.
    log.debug(f'{indent} Compare {left} vs {right}')
    if type(left) is int and type(right) is int and left == right:
        level -= 1
        return None # log.debug(f'{indent} both are ints. Dont return anything. Keep comparing.')
    elif type(left) is int and type(right) is int and left < right:
        log.debug(f'{indent} Left is smaller. Order good.')
        level -= 1
        return True
    elif type(left) is int and type(right) is int and left > right:
        log.debug(f'{indent} Left is larger. Order bad.')
        level -= 1
        return False
    elif type(left) is int and type(right) is list:
        log.debug(f'{indent} Mixed types. Convert left and compare sub items.')
        level -= 1
        return left_side_is_smaller([left], right)
    elif type(left) is list and type(right) is int:
        log.debug(f'{indent} Mixed types. Convert right and compare sub items.')
        level -= 1
        return left_side_is_smaller(left, [right])

    else:  # Must be type(left) is list and type(right) is list:
        for sub_left, sub_right in zip(left, right):
            sub_ret = left_side_is_smaller(sub_left, sub_right)
            if sub_ret is not None:
                level -= 1
                return sub_ret

        # If we got to this point, then one of the lists is longer than the other.
        if len(left) < len(right):
            log.debug(f'{indent} Left ran out of items. Order is good.')
            level -= 1
            return True
        elif len(left) > len(right):
            log.debug(f'{indent} Right ran out of items. Order is bad.')
            level -= 1
            return False
        else:
            log.debug(f'{indent} Both lists are the same length. Keep comparing.')


    level -= 1
    return ret

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

    # Prefix log output with timestamps
    default_date_format = '%Y-%m-%d %H:%M:%S'
    default_log_format = '%(levelname)s: %(message)s'

    # A named logger lets us add more handlers if/when needed.
    log = logging.getLogger("foo")

    # Set the minimum threshold needed by any handler, then override desired levels for each handler.
    # If this is set to "CRITICAL", for instance, nothing will ever appear in any log handler.
    log.setLevel(logging.DEBUG)

    # Set up handler for terminal logging
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setLevel(level)  # Let terminal log level be controlled by args
    console_handler.setFormatter(logging.Formatter(default_log_format, datefmt=default_date_format))
    log.addHandler(console_handler)

    main(data)
