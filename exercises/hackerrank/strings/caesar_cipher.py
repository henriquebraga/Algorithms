#!/bin/python3

import math
import os
import random
import re
import sys

import string

'''
Problem: https://www.hackerrank.com/challenges/caesar-cipher-1
'''

LETTERS_LOWER_CASE = tuple(string.ascii_lowercase)   
LETTERS_UPPER_CASE = tuple(string.ascii_uppercase)


ASCII_LETTER_LOWER_START = 97
ASCII_LETTER_UPPER_START = 65


def caesarCipher(s, k): 
    return ''.join([encrypt_char(char) for char in s])


def encrypt_char(char):
    if char.islower():
        return LETTERS_LOWER_CASE[(ord(char) - ASCII_LETTER_LOWER_START + k) % 26]
    elif char.isupper():
        return LETTERS_UPPER_CASE[(ord(char) - ASCII_LETTER_UPPER_START + k) % 26]
    return char

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
