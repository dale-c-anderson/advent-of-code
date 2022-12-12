#!/usr/bin/env python3
"""
AdventOfCode.com 2022, Day 12
"""

__author__ = "Dale Anderson"

import argparse
import logging
import sys


def main(data0):

    if args.part1 or not args.part2:
        part1_answer = part1(data0)
        print(f'Part 1: {part1_answer}')

    if args.part2 or not args.part1:
        part2_answer = part2(data0.splitlines())
        print(f'Part 2: {part2_answer}')


def parse_input(data):
    global grid
    grid = []
    for y, line in enumerate(data.splitlines()):
        grid.append([])
        for x, char in enumerate(line):
            grid[y].append((char, 0))
    for line in grid:
        for char, visits in line:
            print(char, end='')
        print()

    for line in grid:
        for char, visits in line:
            print(visits, end='')
        print()


def part1(data):
    parse_input(data)
    global positions_visited
    positions_visited = []
    startx, starty = find_single_pos('S')
    positions_visited.append((startx, starty))
    log.debug(f'positions_visited: {positions_visited}')
    endx, endy = find_single_pos('E')
    while not (endx, endy) in positions_visited:
        move_to_higher_letter()
    return len(positions_visited)


def move_to_higher_letter():
    global grid
    global positions_visited
    #log.debug(positions_visited)
    startx, starty = positions_visited[-1]
    current_char = grid[starty][startx]
    if current_char == 'S':
        current_char = 'a'
    # log.debug(f' current_char: {current_char}, startx: {startx}, starty: {starty}')

    for x, y in (0,1) , (1,0), (-1,0), (0,-1):
        check_x = startx + x  # chars
        check_y = starty + y  # lines
        if check_x < 0 or check_y < 0 or check_x >= len(grid[0]) or check_y >= len(grid):
            log.debug(f'  check x: {check_x}, y: {check_y}, out of bounds')
            continue

        char_at_check_pos = grid[check_y][check_x]
        if ord(char_at_check_pos) - ord(current_char) == 1:  # Step up to next level
            log.debug(f'  found higher letter {char_at_check_pos} at {check_x},{check_y}')
            if not (check_x, check_y) in positions_visited:
                # never visit the same position twice
                positions_visited.append((check_x, check_y))
                return
        elif ord(char_at_check_pos) - ord(current_char) == 53:  # We found 'E' from 'z'
            log.debug(f'  found exit at {check_x},{check_y}')
            positions_visited.append((check_x, check_y))
            return
        elif ord(char_at_check_pos) - ord(current_char) in (1, 0):  # Neither a step up or the end was found, but same level was found, so keep going.
            if not (check_x, check_y) in positions_visited:
                # never visit the same position twice
                log.debug(f'  found same level {char_at_check_pos} at {check_x},{check_y}')
                positions_visited.append((check_x, check_y))
                return
            log.debug(f'  found same level {char_at_check_pos} at {check_x},{check_y}, but we were ')


    log.debug(f'  check x: {check_x}, y: {check_y}, char {char_at_check_pos} is not better than {current_char}. Removing last position visited.')

    # If we get to this step, it means we have not finished, and no better char was found, so:
    positions_visited.pop()    # - Move the cursor to the previous position, so we can try again.
    grid[starty][startx] = '.' # - "Burn" the current position so it can't be moved to again.

def find_single_pos(needle):
    global grid
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == needle:
                return x, y



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
