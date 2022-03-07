#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    closing_brackets = {
        ']': '[',
        '}': '{',
        ')': '(',
    }
    
    open_brackets = []
    
    for bracket in s:
        if bracket in ('[', '{', '('):
            open_brackets.append(bracket)
        else:
            if len(open_brackets) == 0:
                return 'NO'
            
            last_open_bracket = open_brackets.pop()

            if last_open_bracket != closing_brackets[bracket]:
                return 'NO'
    if len(open_brackets) == 0:
        return 'YES'
    return 'NO'
    
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
