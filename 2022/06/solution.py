#!/usr/bin/env python3
"""
Advent of Code (AoC) 2022, Day 06
"""

__author__ = "Dale Anderson"


def main():
    handle = open("./input")
    data = handle.read()

    part1_answer = solution(data, buffer_size=4)
    print(f'Part 1: {part1_answer}')

    part2_answer = solution(data, buffer_size=14)
    print(f'Part 2: {part2_answer}')


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


if __name__ == "__main__":
    main()
