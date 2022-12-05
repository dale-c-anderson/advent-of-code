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
    data = handle.read().split('\n\n')
    container_blob = data[0]
    #log.debug(f'{container_blob}')
    stacks = make_stacks(container_blob)
    # log.debug(f'stacks before all moves {stacks}')
    instructions = data[1].split('\n')
    new_stacks = move_stacks(stacks, instructions)
    log.debug(f'stacks after all moves {new_stacks}')

    answer = ''
    for stack in new_stacks:
        top_container = new_stacks[stack][0]
        answer = f'{answer}{top_container}'

    print(answer)
    # moves = data[1].split('\n')
    # log.debug(f'stacks: {stacks}')
    # #log.debug(f'moves: {moves}')

def move_stacks(stacks, moves):
    for move in moves:
        if move.strip() == '':
            continue
        log.debug(f'{move}')
        a = move.split(' ')
        num = a[1]
        #log.debug(f'num: {num}')
        from_stack = str(a[3])
        #log.debug(f'from_stack: {from_stack}')
        to_stack = str(a[5])
        #log.debug(f'to_stack: {to_stack}')
        intermediate = []
        log.debug(f'BEFORE from: {stacks[from_stack]}')
        log.debug(f'BEFORE to  : {stacks[to_stack]}')
        for i in range(int(num)):
            container = stacks[str(from_stack)].pop(0)
            #log.debug(f'container: {container}')
            #log.debug(f'stacks[from_stack]: {stacks[from_stack]}')
            intermediate.append(container)

        #log.debug(f'intermediate: {intermediate}')
        stacks[str(to_stack)] = intermediate + stacks[str(to_stack)]
        log.debug(f'AFTER from: {stacks[from_stack]}')
        log.debug(f'AFTER to  : {stacks[to_stack]}')
        #log.debug(f'STACKS after move {stacks}')
        log.debug('\n\n\n')



    return stacks

def make_stacks(blob):
    stacks = {}
    row_i = 0
    for row in reversed(blob.split('\n')):
        #log.debug(f'row: {row}')
        column_width = 4
        chunks = [row[i:i+column_width] for i in range(0, len(row), column_width)]
        #log.debug(f'chunks: {chunks}')
        stack_i = 1
        for chunk in chunks:
            container = chunk.strip().replace('[', '').replace(']', '')
            #log.debug(f'container: {container}')
            if row_i == 0:
                stacks[f"{container}"] = []
            #log.debug(f'chunk: {chunk}, stack_i: {stack_i}')
            if container != '':
                stacks[str(stack_i)].insert(0, container)
            stack_i += 1
        row_i += 1
        #log.debug(f'stacks: {stacks}')
        #log.debug('\n\n')
    return stacks


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
