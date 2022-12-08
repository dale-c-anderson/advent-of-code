#!/usr/bin/env python3
"""
AdventOfCode.com 2022, Day 08
"""

__author__ = "Dale Anderson"

import argparse
import logging
import sys


def main():
    handle = open("./input")
    data = handle.read().split('\n')
    data = list(filter(None, data))  # get rid of empty rows

    #log.debug(data)

    part1_answer = part1(data)
    print(f'Part 1: {part1_answer}')

    part2_answer = part2(data)
    print(f'Part 2: {part2_answer}')


def part1(data):
    col_count = len(data[0])
    columns = [None] * col_count

    # Populate column arrays
    for row_index, line in enumerate(data):
        for col_index, char in enumerate(line):
            if row_index == 0:
                columns[col_index] = []
            columns[col_index].append(char)

    # Calculate visibility
    visible_trees = 0
    for row_index, row_as_string in enumerate(data):
        row_as_list = list(row_as_string)
        for col_index, char in enumerate(row_as_string):
            height = int(char)


            trees_on_top = columns[col_index][0:row_index]
            log.debug(f'f trees_on_top {trees_on_top}')

            trees_to_left = row_as_list[0:col_index]
            log.debug(f' trees_to_left {trees_to_left}')

            log.debug(f'height {height}')

            trees_to_right = row_as_list[col_index + 1:]
            log.debug(f'f trees_to_right {trees_to_right}')

            trees_on_bottom = columns[col_index][row_index + 1:]
            log.debug(f'f trees_on_bottom {trees_on_bottom}')

            if all(height > int(x) for x in trees_to_left) \
                    or all(height > int(x) for x in trees_to_right) \
                    or all(height > int(x) for x in trees_on_top) \
                    or all(height > int(x) for x in trees_on_bottom):
                visible_trees += 1
                log.debug(f'tree at {row_index},{col_index} is visible')
            else:
                log.debug(f'tree at {row_index},{col_index} is hidden')

            log.debug('')

        log.debug('')
        log.debug(f'--- new row. Visible trees so far: {visible_trees} --- ')
        log.debug('')

    return visible_trees

def part2(data):
    return 0

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
