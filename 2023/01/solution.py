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
        numbers_only = ''.join([i for i in line if i.isdigit()])
        first_digit = numbers_only[0]
        last_digit = numbers_only[-1]
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

    running_total = 0
    for line in data:
        log.debug(f"line {line}")
        first_digit = find_first_digit(line)
        log.debug(f"first_digit: {str(first_digit)}")
        last_digit = find_last_digit(line)
        log.debug(f"last_digit: {str(last_digit)}")
        two_digit_number = int(str(first_digit) + str(last_digit))
        log.debug(f"two_digit_number: {str(two_digit_number)}")
        running_total += two_digit_number
        log.debug(f"running_total: {str(running_total)}\n\n")
    return running_total

def find_first_digit(line):
    new_line = ''
    for char in line:
        new_line += char
        if char.isdigit():
            return int(char)
        else:
            test = return_number_from_word(new_line)
            if test is not None:
                return test

    raise ValueError('No digits found in line')


def find_last_digit(line):
    backwards_line = line[::-1]
    backwards_new_line = ''
    for char in backwards_line:
        backwards_new_line += char
        if char.isdigit():
            return int(char)
        else:
            forward_word = backwards_new_line[::-1]
            test = return_number_from_word(forward_word)
            if test is not None:
                return test
    raise ValueError('No digit found in line')


def return_number_from_word(haystack):
    if 'one' in haystack:
        return 1
    if 'two' in haystack:
        return 2
    if 'three' in haystack:
        return 3
    if 'four' in haystack:
        return 4
    if 'five' in haystack:
        return 5
    if 'six' in haystack:
        return 6
    if 'seven' in haystack:
        return 7
    if 'eight' in haystack:
        return 8
    if 'nine' in haystack:
        return 9
    return None



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
