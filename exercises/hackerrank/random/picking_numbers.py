#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    """
        Problem: https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true

        The idea here is:
        * Count the occurrences of each number;
        * Find the occurrences from previous (i - 1) and next number (i + 1) (because we need items with at max 1 in difference)
        * Take the max from previous and next number add up with n
        * If the max_sub_array is lower than the sum, we just change it to the new value.
        Performance: O(n)
    """
    occurrences_of_n = {}
    max_sub_array = 0
    for n in a:
        occurrences_of_n[n] = occurrences_of_n.setdefault(n, 0) + 1

    for n in set(a):
        current_sub_array = occurrences_of_n[n] + max(
            occurrences_of_n.get(n + 1, 0),
            occurrences_of_n.get(n - 1, 0),
        )

        if max_sub_array < current_sub_array:
            max_sub_array = current_sub_array
    return max_sub_array


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

