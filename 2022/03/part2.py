#!/usr/bin/env python3
"""
Advent of Code (AoC) boilerplate script for daily puzzles
"""

__author__ = "Dale Anderson"
__version__ = "0.1.0"
__license__ = "GPLv3"

import argparse
import logging
import sys


def main():
    handle = open("./input")
    rucksacks = handle.read().split('\n')
    rucksacks = list(filter(None, rucksacks))
    total = 0
    sets_of_3_bags = []
    log.debug(f'len(rucksacks): {len(rucksacks)}')
    for i in range(0, len(rucksacks), 3): 
        sets_of_3_bags.append(rucksacks[i:i+3]) 

    for triplet in sets_of_3_bags:
        log.debug(f'triplet: {triplet}')
        common = list(set(triplet[0]) & set(triplet[1]) & set(triplet[2]))
        log.debug(f'common: {common}')
        letter_score = score(common[0])
        log.debug(f'score: {letter_score}')
        total += letter_score

    print(f'total: {total}')

def score(letter):
    if letter.isupper():
        val = ord(letter) - 64 + 26
    elif letter.islower():
        val = ord(letter) - 96
    else:
        raise ValueError(f'Invalid letter: {letter}')
    log.debug(val)
    return val

def splitstring(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    return string1, string2

if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=1,
        help="Verbosity (-v, -vv, etc)")
    args = parser.parse_args()

    # Let terminal operator control the logging level sent to stderr
    levels = [
        logging.WARNING,
        logging.INFO,
        logging.DEBUG,
    ]
    level = levels[min(args.verbose, len(levels) - 1)]

    ##################################
    # DO NOT SET basicConfig.
    # Since we have handlers with individual log levels, using basicConfig will ruin everything.
    ###################################
    # logging.basicConfig()
    #     datefmt='%Y-%m-%d %H:%M:%S',
    # )

    default_date_format = '%Y-%m-%d %H:%M:%S'
    default_log_format = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s/%(funcName)s(): %(message)s'

    # Create our own custom logging configuration. Don't use the built-in automagic stuff.
    log = logging.getLogger("foo")

    # Set the minimum threshold needed by any handler, then override desired levels for each handler.
    # If this is set to "CRITICAL", for instance, nothing will ever appear in any log handler.
    log.setLevel(logging.DEBUG)

    # Set up handler for terminal logging
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setLevel(level)  # Let terminal log level be controlled by args
    console_handler.setFormatter(logging.Formatter(default_log_format, datefmt=default_date_format))
    log.addHandler(console_handler)

    main()
