#!/bin/python3

import os
import sys


#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    """
    Problem: https://www.hackerrank.com/challenges/electronics-shop/problem
    Based on: https://github.com/RyanFehr/HackerRank/blob/master/Algorithms/Implementation/Electronics%20Shop/Solution.java

    Explanation

    * Sort keyboard in descending order;
    * Sort drives in ascending order;
    * Iterate over them, but not checking past drives, since keyboard is already greater than b.
    * Performance: O(n log(n))
    """

    keyboards.sort(reverse=True)
    drives.sort()
    best_target = -1

    j = 0

    for i in range(len(keyboards)):
        while j < len(drives):
            if (keyboards[i] + drives[j]) > b:
                break
            if (keyboards[i] + drives[j]) > best_target:
                best_target = keyboards[i] + drives[j]
            j += 1
    return best_target


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
