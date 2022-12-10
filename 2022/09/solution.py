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
    # log.debug(f'Tails initial: {tails}')
    deltas = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }
    for move_index, move in enumerate(moves):
        direction, head_distance = move.split()
        head_distance = int(head_distance)
        delta = deltas[direction]
        log.info('')
        log.info(f'- Move {move_index + 1}: {direction} { head_distance}')
        for distance_moved_so_far in range(head_distance):
            distance_moved_so_far = int(distance_moved_so_far) + 1  # Just get this into a human form
            log.debug(f'-- Step {distance_moved_so_far} of {head_distance}')

            head = tails[0]  # Very first tail is actually head.
            hx, hy = head[-1]  # Current position is last item in the list
            hx_new = hx + delta[0]
            hy_new = hy + delta[1]
            tails[0].append([hx_new, hy_new])  # Record the new position
            log.debug(f'-- Moved head to {hx_new}, {hy_new}. Head positions: {tails[0]}')

            keep_checking_tails = True
            for tail_index, tail_pos_list in enumerate(tails):
                if tail_index > 0:  # Don't count the head as a tail
                    if keep_checking_tails:  # Once one tail stops moving, none of the others will either.
                        relative_head_index = tail_index - 1
                        log.debug(f'--- Checking tail index {tail_index}')
                        log.debug(f'          n       x, y')
                        relative_head = tails[relative_head_index]   # For tail 1, this will actually be head.
                        head_positions = relative_head[-1]
                        #log.debug(f'    Head {relative_head_index} positions: {head_positions}')
                        hx, hy = head_positions
                        log.debug(f'---- Relative head {relative_head_index} is at {hx}, {hy}')

                        this_tail = tails[tail_index]
                        tx, ty = this_tail[-1]  # Last tail position recorded
                        log.debug(f'---- Tail {tail_index} is at {tx}, {ty}')

                        tx_new, ty_new = tx, ty  # Set a default in case this tail doesn't need to move

                        if hx < tx -1 and hy > ty + 1:   # 2x + 2y away
                            tx_new = hx + 1
                            ty_new = hy - 1
                            log.info(' --- Moving tail left and up')
                        elif hx < tx - 1 and hy < ty - 1:   # 2x + 2y away
                            tx_new = hx + 1
                            ty_new = hy + 1
                            log.info(' --- Moving tail left and down')
                        elif hx > tx + 1 and hy > ty + 1:  # 2x + 2y away
                            tx_new = hx - 1
                            ty_new = hy - 1
                            log.info(' --- Moving tail right and up')
                        elif hx > tx + 1 and hy < ty - 1:  # 2x + 2y away
                            tx_new = hy - 1
                            ty_new = hx + 1
                            log.info(' --- Moving tail right and down')
                        elif hx + 1 < tx:
                            tx_new = hx + 1
                            ty_new = hy
                            log.info('Moving tail left')
                        elif hx - 1 > tx:
                            tx_new = hx - 1
                            ty_new = hy
                            log.info('Moving tail right')
                        elif hy - 1 > ty:
                            tx_new = hx
                            ty_new = hy - 1
                            log.info('Moving tail up')
                        elif hy + 1 < ty:
                            tx_new = hx
                            ty_new = hy + 1
                            log.info('Moving tail down')

                        if [tx_new, ty_new] != [tx, ty]:
                            log.debug(f'--- Tail {tail_index} now {tx_new}, {ty_new} (moved)')
                        else:
                            keep_checking_tails = False
                            log.debug(f'--- Tail {tail_index} not moved - tail checking turning off')
                        tails[tail_index].append([tx_new, ty_new])  # "Tail"
                        log.info(f' --- Tails: {list(tail[-1] for tail in tails)}')
                        log.info('')


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
