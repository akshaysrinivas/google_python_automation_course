#!/usr/bin/env python3

import re

def swapper(name):
    if name.isnumeric():
        return "Wrong input"

    pattern = r"([\w\.-]+), ([\w\.-]+)"
    result = re.search(pattern, name)
    if result is None:
        return name
    
    return "{}, {}".format(result[2], result[1])

input_name = input("Enter your name : ")
