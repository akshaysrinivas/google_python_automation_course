#!/usr/bin/env python3

def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1


list = ["akshay", "goat", "cow", "human", "cock", "pussy", "great"]
result = linear_search(list, "cow")
print("{} {}".format(result+1, "Hey"))