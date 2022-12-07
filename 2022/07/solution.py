#!/usr/bin/env python3
"""
AdventOfCode.com 2022, Day 07
"""
__author__ = "Dale Anderson"
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
        parts = command.split(' ')
        if parts[0].isnumeric():
            my_bytes = int(parts[0])
            dir_data[current_dir] += my_bytes

        elif parts[0] == '$':
            command = parts[1]
            if command == 'cd':
                dir_name = parts[2]
                if dir_name == '..':
                    before = current_dir
                    parent_dir = str(Path(before).parent)
                    current_dir = parent_dir
                else:
                    # Must be the name of a directory! "cd" into it.
                    if current_dir == '/':
                        current_dir = f'/{dir_name}'
                    else:
                        current_dir = f'{current_dir}/{dir_name}'
                    if current_dir not in dir_data:
                        dir_data[current_dir] = 0

    # Sum up all subdirectory bytes
    for dir_name, dir_bytes in dir_data.items():
        combined_total = 0
        match_count = 0
        for match_dir_name, match_dir_bytes in dir_data.items():
            if match_dir_name.startswith(dir_name):
                match_count += 1
                combined_total += int(match_dir_bytes)
        if match_count > 1:
            dir_data[dir_name] = combined_total

    return dir_data


def part1(dir_data):
    bytes_limit = 100000
    total = 0
    for dir_name, dir_bytes in dir_data.items():
        if int(dir_bytes) <= bytes_limit:
            total += int(dir_bytes)
    return total


def part2(dir_data):
    current_use = dir_data['/']
    disk_size = 70000000
    min_free_space = 30000000
    min_size_to_delete = current_use - disk_size + min_free_space
    candidates = {}
    for dir_name, dir_bytes in dir_data.items():
        if int(dir_bytes) >= min_size_to_delete:
            candidates[dir_name] = dir_bytes
    smallest_possible = min(candidates.values())
    return smallest_possible


if __name__ == "__main__":
    main()
