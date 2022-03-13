#!/bin/python3

import math
import os
import random
import re
import sys

from heapq import heappush, heappop, heapify 
#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    stack = []
    max_value = -1
    max_values = []

    for operation in operations:
        splitted_op = operation.split(' ')
        el = None
        op = None
        
        if len(splitted_op) == 2:
            op, el = splitted_op[0], splitted_op[1]
        else:
            op = splitted_op[0]
        
        if op == '1':
            if int(el) > max_value: #if element is bigger, reset the max
                max_value = int(el)
            stack.append({'max': max_value, 'element': el})
        if op == '2':
            # if len(stack) > 0:
            #     stack.pop()
            
            if len(stack) == 0: #if stack is empty, reset max_value
                max_value = -1
            else:
                max_value = stack[-1]['max']
    
        if op == '3':
            max_values.append(stack[-1]['max'])
            
    return max_values
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
