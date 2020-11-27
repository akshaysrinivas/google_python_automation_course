#!/usr/bin/env python3

def bsearch(left, right, list_in, key):
    if left < right:
        middle = (left + (right-1))//2
        if list_in[middle] < key:
            return bsearch(middle+1, right, list_in, key)
        elif list_in[middle] > key:
            return bsearch(left, middle-1, list_in, key)
        else:
            return middle
    else:
        return -1

a = [12, 11, 9, 34, 100, 103, 55, 76, 87, 23, 54, 29, 18]
a.sort()
in_value = int(input("\nEnter a number to search in the list :"))

result = bsearch(0, len(a), a, in_value)



if result == -1:
    print("\n Element not in the list.")
else:
    print("\n{}".format(a))
    for i in range(len(a)):
        print(i, end=' ')

    print("\nElement {} found in postion {}.".format(in_value, result))