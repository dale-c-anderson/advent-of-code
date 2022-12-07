#!/usr/bin/env python3
"""
AdventOfCode.com 2022, Day 07
"""

__author__ = "Dale Anderson"

import argparse
import logging
import sys
from pathlib import Path


def main():
    handle = open("./input")
    data = handle.read()

    converted_data = generate_dir_data_from_raw(data)

    part1_answer = part1(converted_data)
    print(f'Part 1: {part1_answer}')

    part2_answer = part2(converted_data)
    print(f'Part 2: {part2_answer}')


def generate_dir_data_from_raw(transcript_raw):
    dir_data = {
        '/': 0
    }
    current_dir = '/'
    transcript = transcript_raw.split('\n')
    for command in transcript:
        # log.debug(f'dir_data: {dir_data}')
        parts = command.split(' ')
        if parts[0] == '':
            log.debug(f'parts 0 is an empty line.')
            pass
        elif parts[0].isnumeric():
            my_bytes = int(parts[0])
            log.debug(f'{current_dir} + {my_bytes} bytes')
            dir_data[current_dir] += my_bytes
            # bytes_now = sum(dir_data.values())
            # if bytes_now > bytes_limit:
            #     return bytes_now

        elif parts[0] == 'dir':
            dir_name = parts[1]
            if current_dir == '/':
                log.debug(f'/{dir_name}')
            else:
                log.debug(f'{current_dir}/{dir_name}')
            # log.debug(f'dir {dir_name}')
            pass # There is nothing to process here.

        elif parts[0] == '$':
            command = parts[1]
            if command == 'ls':
                log.debug(f'{command} {current_dir}')
                pass  # There's nothing to process here.

            elif command == 'cd':
                dir_name = parts[2]
                if dir_name == '/':
                    log.debug('cd / (real root)')
                    pass # There's nothing to process here.
                elif dir_name == '..':
                    before = current_dir
                    parent_dir = str(Path(before).parent)
                    # log.debug(f'cd .. current_dir before {current_dir}')
                    current_dir = parent_dir
                    log.debug(f'cd {current_dir} (calculated). Before: {before}. Parent: {parent_dir}')
                else:
                    # Must be the name of a directory! "cd" into it.
                    if current_dir == '/':
                        current_dir = f'/{dir_name}'
                    else:
                        current_dir = f'{current_dir}/{dir_name}'
                    if current_dir in dir_data:
                        # log.warning(f"Unexpected current dir already exists: {current_dir}")
                        pass
                    else:
                        dir_data[current_dir] = 0
                    log.debug(f'cd {current_dir}')
            else:
                raise ValueError('Unhandled command')
        else:
            raise ValueError('Unhandled Parts[0] condition')

    # # Show dirs before we sum totals
    for dir_name, dir_bytes in dir_data.items():
        log.debug(f'BEFORE {dir_bytes}\t{dir_name}\t')
    log.debug('')

    # Sum up all subdirectory bytes
    for dir_name, dir_bytes in dir_data.items():
        #log.debug(f'Checking {dir_name}')
        combined_total = 0
        match_count = 0
        for match_dir_name, match_dir_bytes in dir_data.items():   # iter on both keys and values
            if match_dir_name.startswith(dir_name):
                #log.debug(f'MATCH   {match_dir_bytes}\t{match_dir_name}\t')
                match_count += 1
                combined_total += int(match_dir_bytes)
        #log.debug('')
        if match_count > 1:
          dir_data[dir_name] = combined_total
        # if f'dir_name' in dir_data.keys():
        #     log.debug(f'FOUND   {dir_bytes}\t{dir_name}\t')
        # else:
        #     log.debug(f'not     {dir_bytes}\t{dir_name}\t')

    #
    log.debug('')
    for dir_name, dir_bytes in dir_data.items():
        log.debug(f'AFTER {dir_bytes}\t{dir_name}\t')

    return dir_data

def part1(dir_data):
    log.debug('')
    bytes_limit = 100000
    total = 0
    for dir_name, dir_bytes in dir_data.items():
        if int(dir_bytes) <= bytes_limit:
            total += int(dir_bytes)
            log.debug(f'INCLUDE {dir_bytes}\t{dir_name}\t')
        else:
            log.debug(f'        {dir_bytes}\t{dir_name}\t')

    return total


def part2(dir_data):
    current_use = dir_data['/']
    disk_size = 70000000
    min_free_space = 30000000
    min_size_to_delete = current_use - disk_size + min_free_space
    total = 0
    candidates = {}
    log.debug(f'total size {disk_size}')
    log.debug(f'used       {current_use}')
    log.debug(f'min free   {min_free_space}')
    log.debug(f'min_del    {min_size_to_delete}')
    for dir_name, dir_bytes in dir_data.items():
        if int(dir_bytes) >= min_size_to_delete:
            candidates[dir_name] = dir_bytes
            log.debug(f'CONSIDER {dir_bytes}\t{dir_name}\t')
        else:
            log.debug(f'         {dir_bytes}\t{dir_name}\t')

    for dir_name, dir_bytes in candidates.items():
        log.debug(f'CANDIDATE {dir_bytes}\t{dir_name}\t')

    smallest_possible = min(candidates.values())
    return smallest_possible



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
