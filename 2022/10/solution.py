#!/usr/bin/env python3
"""
AdventOfCode.com 2022, Day 10
"""

__author__ = "Dale Anderson"

import argparse
import logging
import sys


def main(data0):

    if args.part1 or not args.part2:
        part1_answer = part1(data0.splitlines())
        print(f'Part 1: {part1_answer}')

    if args.part2 or not args.part1:
        part2_answer = part2(data0.splitlines())
        print(f'Part 2: {part2_answer}')


def part1(data1):
    register_value = 1
    op_costs = {
        'noop': 1,
        'addx': 2,
    }
    cycles_left = 0
    cycle_number = -1
    op = None
    signal_strength_sum = 0
    op_value = 0
    while cycles_left > 0 or len(data1) > 0:
        cycle_number += 1
        signal_strength = register_value * cycle_number
        log.debug(f'begin cycle {cycle_number}, left {cycles_left}, op {op}, opval {op_value}'
                  f', register_value {register_value}, signal_strength {signal_strength}'
                  f', signal_strength_sum {signal_strength_sum}, len(data) {len(data1)}'
                  )
        if ((cycle_number -20) % 40 == 0 and cycle_number > 40) or cycle_number == 20:
            log.info(f'------- adding {signal_strength} to {signal_strength_sum} at cycle {cycle_number}')
            signal_strength_sum += signal_strength
            log.info(f'------- new sum {signal_strength_sum}')
        if cycles_left > 1:
            cycles_left -= 1
            continue
        else:
            if op == 'addx':
                log.info(f'           adding {op_value} to {register_value} at cycle {cycle_number}')
                register_value += int(op_value)
                log.info(f'           new register_value {register_value}')
            if len(data1) == 0:
                break
            instruction = data1.pop(0)
            if ' ' in instruction:
                op, op_value = instruction.split(' ')
                log.debug(f'op: {op}, op_value: {op_value}')
            else:
                op = instruction
                log.debug(f'op: {op}')
            cycles_left = op_costs[op]

    return signal_strength_sum


def part2(data2):
    register_value = 1
    op_costs = {
        'noop': 1,
        'addx': 2,
    }
    cycles_left = 0
    cycle_number = -1
    op = None
    signal_strength_sum = 0
    op_value = 0
    while cycles_left > 0 or len(data1) > 0:
        cycle_number += 1
        signal_strength = register_value * cycle_number
        log.debug(f'begin cycle {cycle_number}, left {cycles_left}, op {op}, opval {op_value}'
                  f', register_value {register_value}, signal_strength {signal_strength}'
                  f', signal_strength_sum {signal_strength_sum}, len(data) {len(data1)}'
                  )
        if ((cycle_number -20) % 40 == 0 and cycle_number > 40) or cycle_number == 20:
            log.info(f'------- adding {signal_strength} to {signal_strength_sum} at cycle {cycle_number}')
            signal_strength_sum += signal_strength
            log.info(f'------- new sum {signal_strength_sum}')
        if cycles_left > 1:
            cycles_left -= 1
            continue
        else:
            if op == 'addx':
                log.info(f'           adding {op_value} to {register_value} at cycle {cycle_number}')
                register_value += int(op_value)
                log.info(f'           new register_value {register_value}')
            if len(data1) == 0:
                break
            instruction = data1.pop(0)
            if ' ' in instruction:
                op, op_value = instruction.split(' ')
                log.debug(f'op: {op}, op_value: {op_value}')
            else:
                op = instruction
                log.debug(f'op: {op}')
            cycles_left = op_costs[op]

    return signal_strength_sum


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
