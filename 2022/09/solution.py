#!/usr/bin/env python3
"""
AdventOfCode.com 2022, Day 09
"""

__author__ = "Dale Anderson"

import argparse
import logging
import sys


def main():
    handle = open("./input")
    data = handle.read().splitlines()

    # part1_answer = part1(data)
    # print(f'Part 1: {part1_answer}')

    part2_answer = part2(data)
    print(f'Part 2: {part2_answer}')


def part1(moves):
    head_positions = [
        [0, 0],
    ]
    tail_positions = [
        [0, 0],
    ]
    deltas = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }
    for move in moves:
        direction, distance = move.split()
        delta = deltas[direction]
        log.info(f'Processing {direction} {distance}')
        for _ in range(int(distance)):
            hx, hy = head_positions[-1]
            tx, ty = tail_positions[-1]
            log.debug(f'Current head position: {hx}, {hy}')
            hx_new = hx + delta[0]
            hy_new = hy + delta[1]
            log.debug(f'New head position: {hx_new}, {hy_new}')
            head_positions.append([hx_new, hy_new])
            tx_new, ty_new = tx, ty  # Set a default in case they don't move
            if direction == 'L':
                if hx_new + 1 < tx:
                    tx_new = hx_new + 1
                    ty_new = hy_new
                    log.info('Moving tail left')
            elif direction == 'R':
                if hx_new - 1 > tx:
                    tx_new = hx_new - 1
                    ty_new = hy_new
                    log.info('Moving tail right')
            elif direction == 'U':
                if hy_new - 1 > ty:
                    tx_new = hx_new
                    ty_new = hy_new - 1
                    log.info('Moving tail up')
            elif direction == 'D':
                if hy_new + 1 < ty:
                    tx_new = hx_new
                    ty_new = hy_new + 1
                    log.info('Moving tail down')
            else:
                raise ValueError(f'Unknown direction: {direction}')
            log.debug(f'New tail position: {tx_new}, {ty_new}')
            tail_positions.append([tx_new, ty_new])
            # if [tx_new, ty_new] not in tail_positions:
            #     log.debug(f'New *UNIQUE* tail position: {tx_new}, {ty_new}')
    #log.debug(f'Head positions: {head_positions}')
    #log.debug(f'Tail positions: {tail_positions}')
    unique_tail_positions = set(tuple(i) for i in tail_positions)
    return len(unique_tail_positions)


def part2(moves):
    tails = []
    for i in range(0, 10):
        tails.append([[0, 0]])  # Each tail contains list of positions
    log.debug(f'Tails: {tails}')
    deltas = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }
    for move in moves:
        direction, head_distance = move.split()
        head_distance = int(head_distance)
        delta = deltas[direction]
        log.info(f'- Direction {direction} { head_distance}')
        for distance_moved_so_far in range(head_distance):
            distance_moved_so_far = int(distance_moved_so_far) + 1  # Just get this into a human form
            log.debug(f'-- Distance {distance_moved_so_far} of {head_distance}')
            # Real head position
            head_positions = tails[0]  # Very first tail is actually head.
            hx, hy = head_positions[-1]  # Last position in list.
            hx_new = hx + delta[0]
            hy_new = hy + delta[1]
            log.debug(f'--- Head now {hx_new}, {hy_new}')
            tails[0].append([hx_new, hy_new])  # Very first tail is actually head.
            keep_checking_tails = True
            for tail_index, tail_pos_list in enumerate(tails):
                #log.debug(f'--- Decision: tail_index {tail_index}, distance_moved_so_far {distance_moved_so_far}, keep_checking_tails {keep_checking_tails}, ')
                if (tail_index > 0):  # Don't count the head as a tail
                    log.debug(f'--- Checking tail {tail_index}')
                    if True or keep_checking_tails:  # Once one tail stops moving, none of the others will either.
                        this_tail = tails[tail_index]
                        tx, ty = this_tail[-1]  # Last tail position recorded
                        previous_tail = tails[tail_index - 1]   # For tail 1, this will actually be head.
                        px, py = previous_tail[-1]
                        tx_new, ty_new = tx, ty  # Set a default in case this tail doesn't need to move
                        if direction == 'L':
                            if px + 1 < tx:
                                tx_new = px + 1
                                ty_new = py
                                log.info(f'Moving tail {tail_index} left')
                        elif direction == 'R':
                            if px - 1 > tx:
                                tx_new = px - 1
                                ty_new = py
                                log.info(f'Moving tail {tail_index} right')
                        elif direction == 'U':
                            if py - 1 > ty:
                                tx_new = px
                                ty_new = py - 1
                                log.info(f'Moving tail {tail_index} up')
                        elif direction == 'D':
                            if py + 1 < ty:
                                tx_new = px
                                ty_new = py + 1
                                log.info(f'Moving tail {tail_index} down')
                        else:
                            raise ValueError(f'Unknown direction: {direction}')

                        if [tx_new, ty_new] != [tx, ty]:
                            log.debug(f'--- Tail {tail_index} now {tx_new}, {ty_new} (moved)')
                        else:
                            log.debug(f'--- Tail {tail_index} now {tx_new}, {ty_new}')
                            keep_checking_tails = False
                        tails[tail_index].append([tx_new, ty_new])  # "Tail"
                        log.debug('')
        log.debug(f'Tails: {list(tail[-1] for tail in tails)}')
        log.debug('')


    tail_positions = tails[9]  # == tail no. 9, since tail 0 is head.
    unique_tail_positions = set(tuple(i) for i in tail_positions)
    return len(unique_tail_positions)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
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
