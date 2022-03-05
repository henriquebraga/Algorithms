class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.value if self.first else None

    def enqueue(self, value):
        node = Node(value)
        
        if self.length == 0:
            self.first = node
            self.last = node

        else:
            self.last.next = node
            self.last = node

        self.length += 1

    def dequeue(self):
        if self.first is None:
            return None

        value = self.first.value
        self.first = self.first.next
        
        self.length -= 1

        return value

    def is_empty(self):
        return self.length == 0

    def __len__(self):
        return self.length


if __name__ == '__main__':

    #queue initial state

    queue = Queue()

    assert len(queue) == 0

    assert queue.first is None
    assert queue.last is None

    #is_empty behaviour

    assert queue.is_empty() is True

    #peek behaviour

    assert queue.peek() is None
 
    #enqueue behaviour

    queue.enqueue(1)
    
    assert len(queue) == 1

    assert queue.first.value == 1
    assert queue.last.value == 1

    assert queue.is_empty() is False

    assert queue.peek() == 1

    queue.enqueue(2)

    assert len(queue) == 2
    
    assert queue.first.value == 1
    assert queue.last.value == 2
    
    #dequeue behaviour

    assert queue.dequeue() == 1

    assert len(queue) == 1
    assert queue.peek() == 2

    assert queue.dequeue() == 2
    assert len(queue) == 0

    assert queue.dequeue() is None
    assert queue.is_empty() is True