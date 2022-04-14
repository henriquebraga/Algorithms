#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#


"""
    Problem: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
    Performance: O(N)
"""

def beautifulDays(i, j, k):
    count = 0
    for day in range(i, j + 1):
        reversed_day = int(str(day)[::-1])
        count += 1 if abs(day - reversed_day) % k == 0 else 0
    return count
    #print(i, j, k)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
