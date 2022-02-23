#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
# Lin for problem

def anagram(s):
    changes = 0

    if len(s) % 2 != 0:
        return - 1

    mid = len(s) // 2
    
    changes = mid

    s_start = s[:mid]
    s_end = list(s[mid:])
    
    for letter in s_start:
        try:
            index = s_end.index(letter)
            changes -= 1
            s_end.pop(index)
            
        except ValueError:
            pass
        
    return changes