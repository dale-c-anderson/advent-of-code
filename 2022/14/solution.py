#!/usr/bin/env python3
"""
AdventOfCode.com 2022, Day 14
"""

__author__ = "Dale Anderson"

import argparse
import logging
import sys
#import numpy as np


def main(data0):

    data0 = data0.splitlines()

    if args.part1 or not args.part2:
        part1_answer = part1(data0)
        print(f'Part 1: {part1_answer}')

    if args.part2 or not args.part1:
        part2_answer = part2(data0)
        print(f'Part 2: {part2_answer}')


def part1(data):
    global rock, sand
    rock = set()
    sand = []
    map_rock(data)
    draw_rock()


def map_rock(lines):
    global rock
    for line_index, line in enumerate(lines):
        plots = line.split(' -> ')
        for plot_index, plot in enumerate(plots):
            if plot_index == 0:
                continue
            # Get our from/to points
            x1, y1 = [int(i) for i in plots[plot_index - 1].split(',')]
            x2, y2 = [int(i) for i in plot.split(',')]
            log.debug(f'{x1},{y1} to {x2},{y2}')
            # Force the end we need to start from to always ben the lower number
            if x1 == x2:
                # Vertical line
                y1, y2 = sorted([y1, y2]) # Force going from low to high
                for y in range(y1, y2 + 1):
                    rock.add((x1, y))
                    log.debug(f'Adding {x1},{y}')
            elif y1 == y2:
                # Horizontal line
                x1, x2 = sorted([x1, x2]) # Force going from low to high
                for x in range(x1, x2 + 1):
                    rock.add((x, y1))
                    log.debug(f'Adding {x},{y1}')
            else:
                raise ValueError(f'Unknown line type: {x1},{y1} to {x2},{y2}')
            #log.debug(f'Rock: {rock}')


def draw_rock():
    global rock
    x_min = min([i[0] for i in rock])
    x_max = max([x for x, y in rock])
    y_min = min([y for x, y in rock])
    y_max = max([y for x, y in rock])
    log.debug(f'x_min: {x_min}, x_max: {x_max}, y_min: {y_min}, y_max: {y_max}')
    for y in range(y_min -1, y_max +1):
        for x in range(x_min - 1, x_max + 1):
            if (x, y) in rock:
                print('#', end='')
            else:
                print(' ', end='')
        print()

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
    default_log_format = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s/%(funcName)s(): %(message)s'

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
