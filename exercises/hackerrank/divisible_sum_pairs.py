#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    divisible_pairs = 0
    
    complements = [0 for n in range(k)]

    for number in ar:
        mod = number % k
        complement_mod = (k - mod) % k
        
        divisible_pairs += complements[complement_mod]
        
        complements[mod] += 1
        
    return divisible_pairs
