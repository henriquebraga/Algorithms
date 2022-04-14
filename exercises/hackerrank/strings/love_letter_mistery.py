#!/bin/python3

import math
import os
import random
import re
import sys
import string
#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    """
    Just converts each letter lower case as an numeric value and calculate sum up the diference between the
    max and min :)
    """
    
    reductions = 0
    
    letters_dict = {letter:i for i,letter in enumerate(string.ascii_letters)}
    
    start = 0
    end = len(s) - 1
    
    while end > start:
        reductions += abs(letters_dict[s[start]] - letters_dict[s[end]])
        start += 1
        end -= 1

    return reductions
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
