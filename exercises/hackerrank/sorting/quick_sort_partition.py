'''
Problem: https://www.hackerrank.com/challenges/insertionsort2/problem
'''

#!/bin/python3

import sys

def quickSort(arr):
    if len(arr) < 2: #base case
        return arr

    #recursive case
    pivot = arr[0]
    smallers = [n for n in arr[1:] if n <= pivot]
    biggers = [n for n in arr[1:] if n > pivot]
    return quickSort(smallers) + [pivot] + quickSort(biggers)


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = quickSort(arr)
    print (" ".join(map(str, result)))


