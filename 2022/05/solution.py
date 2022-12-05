#!/usr/bin/env python3
"""
Advent of Code (AoC) day 5
"""


def main():
    handle = open("./input")
    data = handle.read().split('\n\n')
    container_blob = data[0]
    instructions = data[1].split('\n')

    part1_stacks = move_stacks(container_blob, instructions, preserve_order=False)
    print_answer(part1_stacks)

    part2_stacks = move_stacks(container_blob, instructions, preserve_order=True)
    print_answer(part2_stacks)


def move_stacks(container_data, moves, preserve_order=False):
    stacks = convert_text_data_to_lists(container_data)
    for move in moves:
        if move.strip() == '':
            continue
        a = move.split(' ')
        num = a[1]
        from_stack = str(a[3])
        to_stack = str(a[5])
        intermediate = []
        for i in range(int(num)):
            container = stacks[str(from_stack)].pop(0)
            if preserve_order:
                intermediate.append(container)
            else:
                intermediate.insert(0, container)

        stacks[str(to_stack)] = intermediate + stacks[str(to_stack)]
    return stacks


def convert_text_data_to_lists(blob):
    stacks = {}
    row_i = 0
    for row in reversed(blob.split('\n')):
        column_width = 4
        chunks = [row[i:i+column_width] for i in range(0, len(row), column_width)]
        stack_i = 1
        for chunk in chunks:
            container = chunk.strip().replace('[', '').replace(']', '')
            if row_i == 0:
                stacks[f"{container}"] = []
            if container != '':
                stacks[str(stack_i)].insert(0, container)
            stack_i += 1
        row_i += 1
    return stacks


def print_answer(stacks):
    answer = ''
    for stack in stacks:
        top_container = stacks[stack][0]
        answer = f'{answer}{top_container}'
    print(answer)


if __name__ == "__main__":
    main()
