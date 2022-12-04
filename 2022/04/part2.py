#!/usr/bin/env python3

def main():
    handle = open("./input")
    sa_pairs = list(filter(None, handle.read().split('\n')))
    count = 0
    for pair in sa_pairs:
        sa_elf1, sa_elf2 = pair.split(',')
        if overlaps(sa_elf1, sa_elf2) or overlaps(sa_elf2, sa_elf1):
            count += 1
    print(f"answer: {count}")


def overlaps(a, b):
    a_lb, a_ub = a.split('-')
    b_lb, b_ub = b.split('-')
    return int(a_lb) <= int(b_lb) <= int(a_ub) or int(a_lb) <= int(b_ub) <= int(a_ub)


if __name__ == "__main__":
    main()
