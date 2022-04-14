'''
Problem: https://www.hackerrank.com/challenges/insertionsort2/problem
'''


def convert_to_spaced_str(array):
    return ' '.join(str(n) for n in array)

def is_valid_index(pos):
    return pos >= 0

def has_to_keep_moving_elements(array, key, index_to_compare):
    return is_valid_index(index_to_compare) and key < array[index_to_compare]

def move_number_to_right(array, pos):
    array[pos + 1] = array[pos]


array_size = int(input())
array = [int(n) for n in input().split()]

for i in range(1, array_size):
    key = array[i]
    j = i - 1
    
    while has_to_keep_moving_elements(array, key, j):
        move_number_to_right(array, j)
        j -= 1
    array[j + 1] = key
    
    print(convert_to_spaced_str(array))
