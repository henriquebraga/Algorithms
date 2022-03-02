class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return (
            self.top.value if self.top is not None 
            else None
        )

    def push(self, value):
        node = Node(value)
        
        if self.is_empty():
            self.bottom = node

        node.next = self.top
        self.top = node

        self.length += 1

    def pop(self):
        if self.is_empty():
            return None

        element = self.top

        if self.length - 1 <= 0:
            self.bottom = None

        self.top = self.top.next
        
        self.length -= 1

        return element.value

    def is_empty(self):
        return self.length == 0

    def __len__(self):
        return self.length


if __name__ == '__main__':
    stack = Stack()
    
    assert len(stack) == 0

    assert stack.top is None
    assert stack.bottom is None

    #peek behaviour

    assert stack.peek() is stack.top

    #insert behaviour

    stack.push(1)

    assert len(stack) == 1
    assert stack.top is stack.bottom


    #pop behaviour

    element = stack.pop()

    assert element == 1

    assert len(stack) == 0

    assert stack.top is None
    assert stack.bottom is None

    #is_empty behaviour
    assert stack.is_empty() is True

    #final test

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.peek() == 3
    assert stack.is_empty() is False

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None

