#!/usr/bin/env python3
"""
AdventOfCode.com 2022, Day 08
"""

__author__ = "Dale Anderson"


def main():
    handle = open("./input")
    data = handle.read().split('\n')
    data = list(filter(None, data))  # get rid of empty rows

    part1_answer = part1(data)
    print(f'Part 1: {part1_answer}')

    part2_answer = part2(data)
    print(f'Part 2: {part2_answer}')


def part1(data):
    col_count = len(data[0])
    columns = [None] * col_count

    # Populate column arrays
    for row_index, line in enumerate(data):
        for col_index, char in enumerate(line):
            if row_index == 0:
                columns[col_index] = []
            columns[col_index].append(char)

    # Calculate visibility
    visible_trees = 0
    for row_index, row_as_string in enumerate(data):
        row_as_list = list(row_as_string)
        for col_index, char in enumerate(row_as_string):
            height = int(char)
            trees_on_top = columns[col_index][0:row_index]
            trees_to_left = row_as_list[0:col_index]
            trees_to_right = row_as_list[col_index + 1:]
            trees_on_bottom = columns[col_index][row_index + 1:]
            if all(height > int(x) for x in trees_to_left) \
                    or all(height > int(x) for x in trees_to_right) \
                    or all(height > int(x) for x in trees_on_top) \
                    or all(height > int(x) for x in trees_on_bottom):
                visible_trees += 1
    return visible_trees


def part2(data):
    col_count = len(data[0])
    columns = [None] * col_count

    # Populate column arrays
    for row_index, line in enumerate(data):
        for col_index, char in enumerate(line):
            if row_index == 0:
                columns[col_index] = []
            columns[col_index].append(char)

    # Calculate scenic score
    max_scenic_score = 0
    for row_index, row_as_string in enumerate(data):
        row_as_list = list(row_as_string)
        for col_index, char in enumerate(row_as_string):
            height = int(char)
            trees_on_top = reversed(columns[col_index][0:row_index])
            viewing_distance_top = find_distance(height, trees_on_top)
            trees_to_left = reversed(row_as_list[0:col_index])
            viewing_distance_left = find_distance(height, trees_to_left)
            trees_on_bottom = columns[col_index][row_index + 1:]
            viewing_distance_bottom = find_distance(height, trees_on_bottom)
            trees_to_right = row_as_list[col_index + 1:]
            viewing_distance_right = find_distance(height, trees_to_right)
            scenic_score = viewing_distance_left * viewing_distance_right \
                           * viewing_distance_top * viewing_distance_bottom
            if scenic_score >= max_scenic_score:
                max_scenic_score = scenic_score
    return max_scenic_score


def find_distance(height, trees):
    distance = 0
    for candidate in trees:
        distance += 1
        if int(height) <= int(candidate):
            break
    return distance


if __name__ == "__main__":
    main()
