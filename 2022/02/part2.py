#!/usr/bin/env python3
"""
Document Description
"""

__author__ = "Dale Anderson"
__version__ = "0.1.0"
__license__ = "GPLv3"

import argparse
from logging.handlers import SysLogHandler
import logging
import sys
import re
# import datetime
# import subprocess
# import boto3
# import re
# from functools import lru_cache


def main():
    handle = open("./input.txt")
    data = handle.read()

    rock = 'A'
    paper = 'B'
    scissors = 'C'
    
    lose = 'X'
    draw = 'Y'
    win = 'Z'

    rock_play_points = 1
    paper_play_points = 2
    scissors_play_points = 3

    win_points = 6
    draw_points = 3

    games = data.split('\n')
    games = list(filter(None, games))

    my_points = 0
    for game in games:
        op_play, desired_outcome = game.split(' ')
        log.info(f'op {op_play} me {desired_outcome}')

        if op_play == rock:
            if desired_outcome == win:
                my_play = paper
            elif desired_outcome == draw:
                my_play = rock
            elif desired_outcome == lose:
                my_play = scissors
        elif op_play == paper:
            if desired_outcome == win:
                my_play = scissors
            elif desired_outcome == draw:
                my_play = paper
            elif desired_outcome == lose:
                my_play = scissors
        elif op_play == scissors:
            if desired_outcome == win:
                my_play = rock
            elif desired_outcome == draw:
                my_play = scissors
            elif desired_outcome == lose:
                my_play = paper


        # Add win/lose/draw points
        if op_play == my_play:
            my_points += draw_points
            log.info("draw")
        if op_play == rock:
            if my_play == paper:
                my_points += win_points
                log.info("paper beats rock, i win")
        elif op_play == paper:
            if my_play == scissors:
                my_points += win_points
                log.info("scissors beats rock, i win")
        elif op_play == scissors:
            if my_play == rock:
                my_points += win_points
                log.info("rock beats scissors, i win")

        if my_play == rock:
            my_points += rock_play_points
        elif my_play == paper:
            my_points += paper_play_points
        elif my_play == scissors:
            my_points += scissors_play_points

        log.info('')

    print(f'{my_points}')


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

    # Set up handler for file logging
    file_handler = logging.FileHandler(re.sub(r'\.py$', '', __file__) + '.log')
    file_handler.setLevel(logging.DEBUG)  # Log everything to file
    file_handler.setFormatter(logging.Formatter(default_log_format, datefmt=default_date_format))
    log.addHandler(file_handler)

    # Set up handler for syslog
    syslog_handler = SysLogHandler('/dev/log')
    syslog_handler.setLevel(logging.WARNING)  # Log warnings or worse to syslog
    syslog_handler.setFormatter(logging.Formatter('%(module)s.%(funcName)s[%(process)d] %(levelname)s: %(message)s'))  # Syslog already timestamps everything
    log.addHandler(syslog_handler)

    main()
