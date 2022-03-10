#!/bin/python3

import math
import os
import random
import re
import sys




# def findDigits(n):
#     return sum([1 for d in str(n) if d!= '0' and n % int(d) == 0])


def findDigits(n):
    """
    r % 10 ----> Gets the digits (E.g: 526 % 10 == 6)
    r % 10 != 0 -----> The digit is zero, so we cannot count and divide
    n % (r % 10) -----> The digit is divisor
    r // 10 -----> Divide to use next digit as iteration (e.g: 526 // 10 = 52 // 10 = 5)
    """

    r = n
    divisible_digits = 0
    while r > 0:
        if r % 10 != 0 and n % (r % 10) == 0:
            divisible_digits += 1
        r = r // 10
            
    return divisible_digits
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
