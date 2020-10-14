#!/usr/bin/env python3

import os
import sys

def character_count(filename):
    character_dict = {}
    #trying to open the file
    try:
        f = open(filename)
    except OSError:
        raise FileNotFoundError("File doesn't exist")

    #Now counting the characters in the file
    for line in f:
        temp = line.split()
        line = "".join(temp)
        for char in line:
            character_dict[char] = character_dict.get(char, 0) + 1
    f.close()
    return character_dict

filename = sys.argv[1]

given_dict = character_count(filename)

large = 0

for char in given_dict.keys():
    if char == '\n':
        print("{:>3} is repeating {} times.".format("\\n", given_dict[char]))
        continue
    print("{:>3} is repeating {} times.".format(char, given_dict[char]))
    if given_dict[char] > large:
        large = given_dict[char]
        large_key = char

print("\nLargest occuring character is <\"{}\">. Its repeating {} times".format(large_key, given_dict[large_key]))
