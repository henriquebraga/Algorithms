class Node:

    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

    def __repr__(self):
        return '<Node value: {}>'.format(self.value)


class DoublyLinkedList:

    def __init__(self, value):
        node = Node(value)

        self.head = node
        self.tail = node

        self.length = 1

    def __len__(self):
        return self.length

    def append(self, value):
        node = Node(value)
        node.previous = self.tail
        self.tail.next = node
        self.tail = node

        self.length += 1

    def prepend(self, value):
        node = Node(value)

        node.next = self.head
        self.head.previous = node #the head will be no longer the head. We must point the previous to the new node
        self.head = node

        self.length += 1

    def insert(self, value, index):
        if index <= 0:
            return self.append(value)
        if index >= self.length:
            return self.append(value)

        node = Node(value)
        leader_node = self._traverse(index - 1)

        node.previous = leader_node
        node.next = leader_node.next

        leader_node.next.previous = node
        leader_node.next = node

        self.length += 1

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.previous = None

            return

        lead_node = self._traverse(max(index - 1, 0))

        not_needed_node = lead_node.next
        lead_node.next = not_needed_node.next

        not_needed_node.next.previous = lead_node

        self.length -= 1

    def _traverse(self, index):
        current_node = None

        if index > (len(self) // 2): #if bigger than half, we traverse starting in previous
            current_node = self.tail
            moves = (self.length - 1) - index # here we just figure out how many times to traverse given we start at the end. We use the length -1, because the index is zero based.

            while moves > 0:
                current_node = current_node.previous
                moves -= 1
        else:
            current_node = self.head
            moves = index

            while moves > 0:
                current_node = current_node.next
                moves -= 1

        return current_node

    def __repr__(self):
        repr = '< DoublyLinkedList \n From head to tail: '

        _next = self.head

        while _next:
            repr += ' {} ->'.format(_next.value)
            _next = _next.next
        repr += ' None >'

        repr += '\n From tail to head: '
        _previous = self.tail

        while _previous:
            repr += ' {} ->'.format(_previous.value)
            _previous = _previous.previous
        repr += ' None >'

        return repr


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList(1)

    #creating doubly linked list behavior

    assert len(doubly_linked_list) == 1

    assert doubly_linked_list.head is doubly_linked_list.tail #should be the same node

    #append doubly linked list behavior
    # 1(head) -> <-2(tail) -> NULL
    doubly_linked_list.append(2)

    assert len(doubly_linked_list) == 2

    assert doubly_linked_list.head.value == 1
    assert doubly_linked_list.head.previous is None

    assert doubly_linked_list.head.next.value == 2

    assert doubly_linked_list.tail.value == 2
    assert doubly_linked_list.tail.previous.value == 1

    #prepend doubly linked list behavior
    #0(head)-> <- 1 -> <-2(tail) -> NULL

    doubly_linked_list.prepend(0)

    assert len(doubly_linked_list) == 3

    assert doubly_linked_list.head.value == 0
    assert doubly_linked_list.head.next.value == 1
    assert doubly_linked_list.head.next.previous.value == 0

    #traverse doubly linked list behavior

    doubly_linked_list.prepend(-1)
    doubly_linked_list.prepend(-2)
    doubly_linked_list.prepend(-3)

    # -3 -><-2 -><- -1 ->0(head)-> <- 1 -> <-2(tail) -> NULL

    #should traverse using previous starting from tail
    node = doubly_linked_list._traverse(4)

    assert node.value == 1

    #should traverse using starting from head

    node = doubly_linked_list._traverse(2)
    assert node.value == -1

    #insert behavior

    doubly_linked_list.insert(3, 3)

    import pdb; pdb.set_trace()

    #remove behavior

    doubly_linked_list.remove(0)
