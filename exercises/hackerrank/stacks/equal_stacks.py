#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

#1,2,1,1
#1,1,2
#1,1
def equalStacks(h1, h2, h3):
    
    sums = [sum(h1), sum(h2), sum(h3)]

    target = min(sum(h1), sum(h2), sum(h3))
    while (
        (target != sums[0] or target != sums[1] or target != sums[2])
    ):
        if sums[0] > target and len(h1) > 0:
            n = h1.pop(0)
            new_sum = sums[0] - n
            
            if new_sum < target: # if lower, we need to change our target
                target = new_sum
            sums[0] = new_sum

        if sums[1] > target and len(h2) > 0:
            n = h2.pop(0)
            new_sum = sums[1] - n
            
            if new_sum < target:
                target = new_sum
            sums[1] = new_sum
            
        if sums[2] > target and len(h3) > 0:
            n = h3.pop(0)
            new_sum = sums[2] - n
            
            if new_sum < target:
                target = new_sum
            sums[2] = new_sum
            
        if len(h1) == 0 or len(h2) == 0 or len(h3) == 0:
            return 0
    return target


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
