#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


'''
Problem: https://www.hackerrank.com/challenges/countingsort2/problem
'''


def countingSort(arr):
    counter = [0] * 100
    
    for i in arr:
        counter[i] += 1
    
    sorted_arr = []
    for number, frequency in enumerate(counter):
        sorted_arr.extend([number] * frequency)
        
    return sorted_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
