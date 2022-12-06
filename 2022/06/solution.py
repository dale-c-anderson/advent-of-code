#!/usr/bin/env python3
"""
Advent of Code (AoC) 2022, Day 06
"""

__author__ = "Dale Anderson"


def main():
    handle = open("./input")
    data = handle.read()

    # My solutions,
    part1_answer = solution(data, buffer_size=4)
    print(f'Part 1: {part1_answer}')

    part2_answer = solution(data, buffer_size=14)
    print(f'Part 2: {part2_answer}')

    # Absorbing knowledge from kids who do it better,
    print(f'Part 1: {try_with_enumerate(data, 4)} - using enumerate instead of for loop')


def solution(data, buffer_size):
    buff = []
    count = 0
    for char in data:
        count += 1
        buff.append(char)
        if len(buff) > buffer_size:
            buff.pop(0)
        if len(buff) >= buffer_size:
            if all_unique(buff):
                break
    return count


def all_unique(buff):
    return len(set(buff)) == len(buff)


# Learned something new from https://github.com/oliver-ni/advent-of-code/blob/master/py/2022/day06.py
# Trying to wrap my brain around how it works
def try_with_enumerate(data, buffer_size):
    for index, value in enumerate(data):
        start_pos = index - buffer_size
        end_pos = index
        sample = data[start_pos:end_pos]
        #print(f'sample: {sample}')
        #print(f'set: {set(sample)}')
        num_unique_chars_in_sample = len(set(sample))
        if num_unique_chars_in_sample == buffer_size:
            return index


if __name__ == "__main__":
    main()
