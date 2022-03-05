#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
"""
1. insert
2. delete one occurence
3. check if any integet is present whose frequency is exactly z. If yes, print 1 else 0
"""
def freqQuery(queries):
    el_occurrences = {}
    el_frequencies = {}
    
    results = []
    
    for op, el in queries:
        if op == 1: #insert
            frequency = el_occurrences.get(el, 0)
            frequency += 1
            el_occurrences[el] = frequency

            previous_frequency = frequency - 1
            
            if previous_frequency > 0: #delete frequency only when there's items with 1 occurrences or more
                #delete previous frequency
                elements_with_previous_frequency = el_frequencies.setdefault(previous_frequency, set())
            
                if el in elements_with_previous_frequency:
                    elements_with_previous_frequency.remove(el)
                
                #update new frequency with element
            el_frequencies.setdefault(frequency, set()).add(el)

        elif op == 2: #delete
            frequency = el_occurrences.get(el, 0) #zero when does not have frequency
            
            if frequency > 0: # only delete when it has frequency
                #delete frequency if exists
                frequency_to_delete = el_frequencies[frequency]

                if el in frequency_to_delete:
                    frequency_to_delete.remove(el)
                if frequency - 1 > 0:
                    el_frequencies.setdefault(frequency - 1, set()).add(el)
                    el_occurrences[el] = frequency - 1
                if frequency - 1 == 0:
                    del el_occurrences[el]                

        else:
            result = 1 if len(el_frequencies.get(el, set())) > 0 else 0
            results.append(result)
    return results

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

