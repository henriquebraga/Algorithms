#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

#N: number of pages the book have
#p: page student wants to turn

def pageCount(n, p):
    if p == 1 or n == p:
        return 0

    if p % 2 == 0 and (n - 1) == p:
        return 0
    
    if n % 2 == 0 and (n - 1) == p:
        return 1
    
    return min(p // 2, (n - p) // 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
