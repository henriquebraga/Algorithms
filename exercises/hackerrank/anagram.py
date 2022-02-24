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
    """
        Problem: https://www.hackerrank.com/challenges/anagram/problem?isFullScreen=true
        
        The idea here is to create a dictionary with first half of the string (start) with letter's frequency.

        Then we iterate over the second string (s_end), asking: 
        "do you have this character?"

        And then when it has, we just decrement one change in changes (which starts with max possibilities to change in order to form an anagram)
        
        When there's the letter in the start array (occurrences > 0), we just decrease the frequency in dictionary (for the next iterations)
        and then decrement one change.

        If occurrences it's zero, we just delete the item from dictionary, since there's no possibilities.
    """
    start_s_counter = {}

    if len(s) % 2 != 0:
        return - 1

    mid = len(s) // 2
    
    changes = mid

    s_start = s[:mid]
    s_end = s[mid:]
            
    for letter in s_start:
        start_s_counter[letter] = start_s_counter.setdefault(letter, 0) + 1
        
    for letter in s_end:
        occurences = start_s_counter.get(letter, 0)
        occurences -= 1        
    
        if occurences >= 0:
            changes -= 1
            start_s_counter[letter] = occurences

        if occurences == 0:
            del start_s_counter[letter]
    return changes        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
