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

    # Count trees...
    visible_trees = 0

    # ... From the left and right ...
    corridor_count = 0
    for row in data:
        corridor_count = corridor_count +1
        from_left = list(row)
        log.debug(f' from_left {from_left}')
        visible_trees = visible_trees + count_trees(from_left)
        log.debug(f'visible_trees so far {visible_trees}')

        corridor_count = corridor_count +1
        from_right = list(reversed(row))
        log.debug(f' from_right {from_right}')
        visible_trees = visible_trees + count_trees(from_right)
        log.debug(f'visible_trees so far {visible_trees}')

    # ... From the top and bottom ...
    for column in columns:
        corridor_count = corridor_count +1
        from_top = column
        log.debug(f' from_top {from_top}')
        visible_trees = visible_trees + count_trees(from_top)
        log.debug(f'visible_trees so far {visible_trees}')

        corridor_count = corridor_count +1
        from_bottom = list(reversed(column))
        log.debug(f' from_bottom = {from_bottom}')
        visible_trees = visible_trees + count_trees(from_bottom)
        log.debug(f'visible_trees so far {visible_trees}')

    # ... Finally, deduplicate the corner trees
    visible_trees = visible_trees - 4

    log.debug(f'corridor_count {corridor_count}')
    return visible_trees


def count_trees(some_list):
    visible_trees = 0
    tallest_tree_height = int(-1)
    tree_count = 0
    for tree_height in some_list:
        tree_count += 1
        tree_height = int(tree_height)
        if tree_height > tallest_tree_height:
            visible_trees += 1
            tallest_tree_height = tree_height
            log.debug(f'tree_height {tree_height}, tree_count {tree_count}, visible_trees {visible_trees}')
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
