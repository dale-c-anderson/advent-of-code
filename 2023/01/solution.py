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
    # example data:
    #   two1nine
    #   eightwothree
    #   abcone2threexyz
    #   xtwone3four
    #   4nineeightseven2
    #   zoneight234
    #   7pqrstsixteen

    new_data = []
    for line in data:
        log.debug(f"Processing: {line}")
        new_line = ''
        for char in line:  # Crawl through the line char by char, replacing numeric words as they appear.
            new_line += char
            log.debug(f"          {new_line}")
            if string_contains_number_word(new_line):
                log.debug(f"Replacing.")
                new_line = replace_word_number_with_digit(new_line)
                log.debug(f"            New: {new_line}")

        log.debug(f"Orig: {line}")
        log.info(f" New: {new_line}")
        new_data.append(new_line)
        log.debug("\n")
    return part1(new_data)


def flip(line):
    return line[::-1]


def string_contains_number_word(haystack):
    if 'one' in haystack:
        return True
    if 'two' in haystack:
        return True
    if 'three' in haystack:
        return True
    if 'four' in haystack:
        return True
    if 'five' in haystack:
        return True
    if 'six' in haystack:
        return True
    if 'seven' in haystack:
        return True
    if 'eight' in haystack:
        return True
    if 'nine' in haystack:
        return True
    return False


def replace_word_number_with_digit(text):
    text = text.replace('one', '1')
    text = text.replace('two', '2')
    text = text.replace('three', '3')
    text = text.replace('four', '4')
    text = text.replace('five', '5')
    text = text.replace('six', '6')
    text = text.replace('seven', '7')
    text = text.replace('eight', '8')
    text = text.replace('nine', '9')
    return text


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
