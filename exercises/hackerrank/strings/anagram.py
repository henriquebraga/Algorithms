#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    if len(s) % 2 == 1:
        return - 1
    
    start_s_counter = {}
    
    mid = len(s) // 2
    replacements = mid
    
    for letter in s[:mid]:
        start_s_counter[letter] = start_s_counter.setdefault(letter, 0) + 1
        
    for letter in s[mid:]:
        occurrences_in_start_s = start_s_counter.get(letter, 0)
        occurrences_in_start_s -= 1

        if occurrences_in_start_s == 0:
            del start_s_counter[letter]
        
        if occurrences_in_start_s >= 0:
            replacements -= 1
            start_s_counter[letter] = occurrences_in_start_s
            
    return replacements


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
