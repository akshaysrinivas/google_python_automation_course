#!/usr/bin/env python3

def binary_search(left, right, key, list_in):
    print("\nEntered the function binary_search() with list {}, Left: {} Right: {}".format(list_in, left, right))
    if right >= left:

        middle = (left + (right-1))//2
        print("\nMiddle position set {}: Element {}".format(middle, list_in[middle]))
        if list_in[middle] == key:
            print("\nFound key {} in postion {}".format(key, middle))
            return middle
        elif key < list_in[middle]:
            print("\nKey {} is less than middle element {}. Changing right side to middle-1, ie {}".format(key, list_in[middle], middle-1))
            return binary_search(left, middle-1, key, list_in)
        else:
            print("\nKey {} is greater than middle element {}. Changing left side to middle+1, ie {}".format(key, list_in[middle], middle+1))
            return binary_search(middle+1, right, key, list_in)
    else:
        print("\nKey element {} not found in the list returning -1.".format(key))
        return -1

a = [23, 11, 56, 99, 46, 2]
a.sort()
result = binary_search(0, len(a)-1, 2, a)

if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array") 

