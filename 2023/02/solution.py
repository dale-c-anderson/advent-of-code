#!/usr/bin/env python3
"""
AdventOfCode.com 2023, Day 02
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
    limits = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    # Example data:
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    # Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    # Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    # Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    # Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

    valid_games = []
    for line in data:
        if len(line) == 0:
            continue
        game_id, game = line.split(': ')
        game_id = game_id.replace('Game ', '')
        rolls = game.split('; ')
        game_is_valid = True
        for roll in rolls:
            cubes = roll.split(', ')
            for cube in cubes:
                number = int(cube.split()[0])
                color = cube.split()[1]
                if color not in limits:
                    game_is_valid = False
                if number > limits[color]:
                    game_is_valid = False
        if game_is_valid:
            valid_games.append(int(game_id))

    return sum(valid_games)


def part2(data):
    game_powers = []
    for line in data:
        if len(line) == 0:
            continue
        game_mins = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        game_id, game = line.split(': ')
        rolls = game.split('; ')
        for roll in rolls:
            cubes = roll.split(', ')
            for cube in cubes:
                number = int(cube.split()[0])
                color = cube.split()[1]
                if number > game_mins[color]:
                    game_mins[color] = number
        game_power = game_mins['red'] * game_mins['green'] * game_mins['blue']
        game_powers.append(game_power)

    return sum(game_powers)


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
