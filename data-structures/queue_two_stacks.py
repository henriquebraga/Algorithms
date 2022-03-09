class Queue:

    def __init__(self):
        self.newest = [] #works like a stack, enqueue here
        self.oldest = [] #when empty, pop from newest and put here (reverting it will work like a queue. Use to peek/dequeue)

    def enqueue(self, data):
        self.newest.append(data)

    def dequeue(self):
        if not self.oldest:
            self._shift()

        return self.oldest.pop()
        
    
    def peek(self):
        if not self.oldest:
            self._shift()

        return self.oldest[-1]

    def _shift(self):
            while self.newest:
                self.oldest.append(self.newest.pop())
     
    def __len__(self):
        return len(self.newest) + len(self.oldest)


if __name__ == '__main__':
    queue = Queue()
    
    assert queue.newest == []
    assert queue.oldest == []

    assert len(queue) == 0

    #enqueue behaviour
    queue.enqueue(1)

    assert queue.newest == [1]
    assert len(queue) == 1

    #peek behaviour
    
    assert queue.peek() == 1
    
    #should move elements to oldest because oldest was empty

    assert queue.newest == []
    assert queue.oldest == [1]

    queue.peek()

    assert queue.oldest == [1]

    #dequeue behavior

    assert queue.dequeue() == 1
    assert len(queue) == 0
    assert queue.newest == []
    assert queue.oldest == []

    queue.enqueue(3)
    queue.enqueue(2)
    queue.enqueue(1)

    assert queue.peek() == 3
    assert queue.dequeue() == 3
    assert queue.dequeue() == 2
    assert queue.dequeue() == 1

