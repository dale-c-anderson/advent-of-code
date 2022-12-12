#!/usr/bin/env python3
"""
AdventOfCode.com 2022, Day 11
"""

__author__ = "Dale Anderson"

import argparse
import logging
import sys
import re


def main(data0):

    if args.part1 or not args.part2:
        part1_answer = part1(data0.split('\n\n'))
        print(f'Part 1: {part1_answer}')

    if args.part2 or not args.part1:
        part2_answer = part2(data0.splitlines())
        print(f'Part 2: {part2_answer}')


def part1(data):
    global monkeys
    monkeys = []
    parse_config(data)
    do_rounds(20)

def parse_config(data):
    global monkeys
    for monkey_config in data:
        lines = monkey_config.splitlines()
        starting_items = lines[1].split(':')[1].split(',')
        starting_items = [int(i) for i in starting_items]
        operation_def = lines[2].split(':')[1].strip()
        divisible_by = int(re.findall(r'\d+', lines[3])[0])
        true_action = int(re.findall(r'\d+', lines[4])[0])
        false_action = int(re.findall(r'\d+', lines[5])[0])
        monkey = {
            'items': starting_items,
            'operation_def': operation_def,
            'mod_test': divisible_by,
            'true_action': true_action,
            'false_action': false_action,
        }
        monkeys.append(monkey)
        log.debug(f'monkey: {monkey}')

def do_rounds(rounds):
    global monkeys
    for round in range(1, rounds):
        log.debug(f'Round {round}')
        for monkey_index, monkey in enumerate(monkeys):
            examine_items(monkey_index, monkey)

def examine_items(monkey_index, monkey):
    global monkeys
    items_to_remove = []
    log.debug(f'  monkey[{monkey_index}]: {monkey}')
    items = monkey['items']
    operation_def = monkey['operation_def']
    mod_test = monkey['mod_test']
    true_action = monkey['true_action']
    false_action = monkey['false_action']
    log.debug(f'   items: {items}')
    log.debug(f'   operation_def: {operation_def}')
    log.debug(f'   mod_test: {mod_test}')
    log.debug(f'   true_action: {true_action}')
    log.debug(f'   false_action: {false_action}')
    for item in items:
        log.debug(f'    item: {item}')
        old_worry_level = item
        new_worry_level = process_worry_level(old_worry_level, operation_def)
        log.debug(f'new_worry_level: {new_worry_level}')
        if new_worry_level % mod_test == 0:
            monkey[true_action].items.append(new_worry_level)
        else:
            monkey[false_action].items.append(new_worry_level)
        items_to_remove.append(item)

    for i in range(items_to_remove):
        log.debug(f'removing {items_to_remove[i]} from monkey {monkey_index}')
        monkeys[monkey_index]['items'].pop(0)   # remove it from this monkey's list.


def process_worry_level(old_worry_level, operation_def):
    log.debug(f' ------------ 89 opecation_def: {operation_def}')
    parts = operation_def.split(' ')
    operator = parts[3]
    value = parts[4]

    old_worry_level = old_worry_level // 3
    log.debug(f' ------------ 93 old_worry_level divided: {old_worry_level}')
    if value == 'old':
        value = old_worry_level
    else:
        value = int(value)
    if operator == '*':
        new_worry_level = old_worry_level * value
    elif operator == '+':
        new_worry_level = old_worry_level + value
    else:
        raise ValueError(f'Unknown operator: {operator}')
    return new_worry_level


def part2(data):
    pass


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