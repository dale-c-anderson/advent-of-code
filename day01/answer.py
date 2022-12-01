#!/usr/bin/env python3
"""
Document Description
"""

__author__ = "Dale Anderson"
__version__ = "0.1.0"
__license__ = "GPLv3"

import argparse
import heapq
from logging.handlers import SysLogHandler
import logging
import sys


def main():
    handle = open("./input.txt")
    my_input = handle.read()
    log.debug(["input", my_input])
    chunks = my_input.split("\n\n")
    sums = []
    for chunk in chunks:
        chunk_list_with_possible_blanks = chunk.split('\n')
        chunk_list = list(filter(None, chunk_list_with_possible_blanks))
        ints = list(map(int, chunk_list))
        my_sum = sum(ints)
        sums.append(my_sum)
    answer_part1 = max(sums)
    log.info(["answer part 1", answer_part1])

    top_3_list = heapq.nlargest(3, sums)
    answer_part2 = sum(top_3_list)
    log.info(["answer, part 2", answer_part2])




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

    # Set up handler for syslog
    syslog_handler = SysLogHandler('/dev/log')
    syslog_handler.setLevel(logging.WARNING)  # Log warnings or worse to syslog
    # Syslog already timestamps everything
    syslog_handler.setFormatter(logging.Formatter('%(module)s.%(funcName)s[%(process)d] %(levelname)s: %(message)s'))
    log.addHandler(syslog_handler)

    main()
