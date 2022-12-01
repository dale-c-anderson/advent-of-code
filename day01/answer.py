#!/usr/bin/env python3
import heapq


def main():
    handle = open("./input.txt")
    my_input = handle.read()
    chunks = my_input.split("\n\n")
    sums = []
    for chunk in chunks:
        chunk_list_with_possible_blanks = chunk.split('\n')
        chunk_list = list(filter(None, chunk_list_with_possible_blanks))
        ints = list(map(int, chunk_list))
        my_sum = sum(ints)
        sums.append(my_sum)

    answer_part1 = max(sums)
    print(["answer part 1", answer_part1])

    top_3_list = heapq.nlargest(3, sums)
    answer_part2 = sum(top_3_list)
    print(["answer, part 2", answer_part2])


if __name__ == "__main__":
    main()
