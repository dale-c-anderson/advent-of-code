#!/usr/bin/env python3
"""
AdventOfCode.com 2022, Day 15
"""

__author__ = "Dale Anderson"

import argparse
# import logging
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
    sensors = set()
    beacons = set()
    cleared = set()
    map = []
    for line in data:
        words = line.split()
        # 0      1    2    3    4       5     6  7   8    9
        # Sensor at x=8, y=7: closest beacon is at x=2, y=10
        sx = int(words[2].replace('x=', '').replace(',', ''))
        sy = int(words[3].replace('y=', '').replace(':', ''))
        bx = int(words[8].replace('x=', '').replace(',', ''))
        by = int(words[9].replace('y=', ''))
        sensors.add((sx, sy))
        beacons.add((bx, by))
        map.append((sx, sy, bx, by))
        taxicab_distance = abs(sx - bx) + abs(sy - by)
        for yi, y in enumerate(range(sy - taxicab_distance, sy + taxicab_distance + 1)):
            # log.debug(f'yi: {yi}, y: {y}')
            if yi <= taxicab_distance:
                xlower = sx - yi
                xupper = sx + yi + 1
            else:
                xlower = sx - (2 * taxicab_distance - yi)
                xupper = sx + (2 * taxicab_distance - yi) + 1
            for x in range(xlower, xupper):
                cleared.add((x, y))
        # log.debug(f'sensor: {sx}, {sy}, beacon: {bx}, {by}, cab distance: {taxicab_distance}')

    # draw_cleared(sensors, beacons, cleared, 'cleared')
    count = 0
    for x, y in cleared:
        if y == 2000000:
            if not (x, y) in sensors:
                if not (x, y) in beacons:
                    count += 1
    return count


def draw_cleared(sensors, beacons, cleared, title):
    # if not at_least_log_level_info():
    #     return
    # log.handlers[0].flush()
    print(f'\n--------- {title} ---------\n')
    x_min = min([x for x, y in cleared])
    x_max = max([x for x, y in cleared])
    y_min = min([y for x, y in cleared])
    y_max = max([y for x, y in cleared])
    # log.debug(f'x_min: {x_min}, x_max: {x_max}, y_min: {y_min}, y_max: {y_max}')
    for y in range(y_min -1, y_max +1):
        for x in range(x_min - 1, x_max + 1):
            if (x, y) in sensors:
                print('S', end='')
            elif (x, y) in beacons:
                print('B', end='')
            elif (x, y) in cleared:
                print('#', end='')
            else:
                print(' ', end='')
        print(f' {y}')

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
    # levels = [
    #     logging.WARNING,
    #     logging.INFO,
    #     logging.DEBUG,
    # ]
    # level = levels[min(args.verbose, len(levels) - 1)]

    # A named logger lets us add more handlers if/when needed.
    # log = logging.getLogger("foo")

    # Set the minimum threshold needed by any handler, then override desired levels for each handler.
    # If this is set to "CRITICAL", for instance, nothing will ever appear in any log handler.
    # log.setLevel(logging.DEBUG)

    # Set up handler for terminal logging
    # console_handler = logging.StreamHandler(sys.stderr)
    # console_handler.setLevel(level)  # Let terminal log level be controlled by args
    # default_log_format = '%(levelname)s %(funcName)s(): %(message)s'
    # console_handler.setFormatter(logging.Formatter(default_log_format))
    # log.addHandler(console_handler)

    main(data)
