#!/usr/bin/env python3

def main():
    handle = open("./input")
    sa_pairs = list(filter(None, handle.read().split('\n')))
    count = 0
    for pair in sa_pairs:
        sa_elf1, sa_elf2 = pair.split(',')
        if fully_contains(sa_elf1, sa_elf2) or fully_contains(sa_elf2, sa_elf1):
            print("fully contained")
            count += 1
        else:
            print("not fully contained")
    print(f"answer: {count}")


def fully_contains(haystack, needle):
    haystack_lb, haystack_ub = haystack.split('-')
    needle_lb, needle_ub = needle.split('-')
    return int(haystack_lb) <= int(needle_lb) and int(haystack_ub) >= int(needle_ub)


if __name__ == "__main__":
    main()
