'''
Problem: https://www.hackerrank.com/challenges/insertionsort1/problem
'''

array_size = int(input())


array = [int(n) for n in input().split()]
i = len(array) - 1

while i >= 0:
    key = array[i] 
    j = i - 1
    
    while j >= 0 and key < array[j]:
        array[j + 1] = array[j]
        j = j - 1
        print(' '.join([str(n) for n in array]))    
    
    array[j + 1] = key
    i = i -1

print(' '.join([str(n) for n in array]))    

    
        
        
        
        
        

