

class Stack:

    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[-1] if len(self.array) > 0 else None

    def push(self, value):
        self.array.append(value)

    def pop(self):
        if self.is_empty():
            return None

        return self.array.pop()

    def is_empty(self):
        return len(self.array) == 0

    def __len__(self):
        return len(self.array)


if __name__ == '__main__':
    stack = Stack()
    
    assert len(stack) == 0

    assert stack.array == []

    #peek behaviour

    assert stack.peek() is None

    #insert behaviour

    stack.push(1)

    assert len(stack) == 1
    assert stack.array == [1]


    #pop behaviour

    element = stack.pop()

    assert element == 1

    assert len(stack) == 0

    #is_empty behaviour
    assert stack.is_empty() is True

    #final test

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.peek() == 3
    assert stack.is_empty() is False
    assert stack.array == [1,2,3]

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None

    assert stack.array == []

