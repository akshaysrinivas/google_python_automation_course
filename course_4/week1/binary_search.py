#!/usr/bin/env python3

def binarySearch (arr, l, r, x): 
    print("\nEntered the function binary_search() with list {}, Left: {} Right: {}".format(arr, l, r))
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l) // 2
        print("\nMiddle position set {}: Element {}".format(mid, arr[mid]))
        # If element is present at the middle itself 
        if arr[mid] == x: 
            print("\nFound key {} in postion {}".format(x, mid))
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1
  
# Driver Code 
arr = [ 2, 3, 4, 10, 40 ] 
x = 2
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array") 