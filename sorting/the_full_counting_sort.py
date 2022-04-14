#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    count = [list() for i in range(len(arr))]
    half = (len(arr) // 2 - 1)

    for i, string in enumerate(arr):
        
        position, string_value = string
        
        if i <= half:
            count[int(position)].append('-')
        else:
            count[int(position)].append(string_value)
        
    print(' '.join([' '.join(strings) for strings in count if len(strings) > 0]))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
