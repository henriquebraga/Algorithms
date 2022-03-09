# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
    Idea here is to have a stack to keep track of the action performed previously
    Another tricky is that you have to append BEFORE changing the text and not AFTER.

    Performance O(N) because varies according to the quantity of queries

    Since it's a stack, pop operation is O(1)
"""
queries = int(input())

state = ''
history = []
history.append(state)


for i in range(queries):
    
    query = input().split(' ')        
    command = query[0]
    
    value = None
        
    if len(query) == 2:
        value = query[1]
    
    if command == '1':
        history.append(state)
        state += value
    elif command == '2':
        history.append(state)
        state = state[:-int(value)]
    elif command == '3':
        print(state[int(value) - 1])
    else:
        state = history.pop()
    
