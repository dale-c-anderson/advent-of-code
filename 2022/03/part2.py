#!/usr/bin/env python3

def main():
    handle = open("./input")
    rucksacks = handle.read().split('\n')
    rucksacks = list(filter(None, rucksacks))
    total = 0
    sets_of_3_bags = []
    for i in range(0, len(rucksacks), 3): 
        sets_of_3_bags.append(rucksacks[i:i+3]) 

    for triplet in sets_of_3_bags:
        common = list(set(triplet[0]) & set(triplet[1]) & set(triplet[2]))
        letter_score = score(common[0])
        total += letter_score

    print(f'total: {total}')


def score(letter):
    if letter.isupper():
        val = ord(letter) - 64 + 26
    elif letter.islower():
        val = ord(letter) - 96
    else:
        raise ValueError(f'Invalid letter: {letter}')
    return val


def split_string(value):
    string1, string2 = value[:len(value)//2], value[len(value)//2:]
    return string1, string2


if __name__ == "__main__":
    main()
