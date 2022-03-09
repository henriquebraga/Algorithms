class MyQueue(object):
    def __init__(self):
        self.newer_on_top_stack = []
        self.older_on_top_stack = []
        
    
    def peek(self):
        if len(self.older_on_top_stack) == 0:
            while len(self.newer_on_top_stack) > 0:
                self.older_on_top_stack.append(self.newer_on_top_stack.pop())
                
        return self.older_on_top_stack[-1]
        
        
    def pop(self):
        if len(self.older_on_top_stack) == 0:
            while len(self.newer_on_top_stack) > 0:
                self.older_on_top_stack.append(self.newer_on_top_stack.pop())
                
        self.older_on_top_stack.pop()

    def put(self, value):
        self.newer_on_top_stack.append(value)
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
