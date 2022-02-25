class Node:
    def __init__(self, value: int, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f'<Node value:{self.value}>'


class LinkedList:

    def __init__(self, value: Node):
        self.head = value
        self.tail = value
        self.length = 1

    def __repr__(self):
        repr = '< LinkedList'

        _next = self.head

        while _next:
            repr += ' {} ->'.format(_next.value)
            _next = _next.next
        repr += ' None >'

        return repr

    def __len__(self):
        return self.length

    def append(self, value: int) -> None:
        node: Node = Node(value=value)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def prepend(self, value: int) -> None:
        node: Node = Node(value=value)
        node.next = self.head
        self.head = node
        self.length += 1

    def insert(self, index: int, value: int):
        if index <= 0:
            return self.prepend(value)
        if index >= self.length:
            return self.append(value)

        _next = self.head

        leader_node = self._traverse(index - 1) # because we need the previous index to change the pointers

        '< LinkedList 10 -> 15 -> 3 -> 5 -> None >'
        inserting_node: Node = Node(value)
        inserting_node.next = leader_node.next  # leader_node: 10 -> 3 -> 5 -> None // Inserting_node: 15 -> 3 -> 5 (points to next element of 10
        leader_node.next = inserting_node #leader_node: 10 -> 15 -> 3 -> 5 (sets the next point from leader to inserting_node)
        self.length += 1

    def remove(self, index):
        if index <= 0:
            return self.pop()


        leader_node = self._traverse(index - 1)
        not_needed_node = leader_node.next
        leader_node.next = not_needed_node.next

        self.length -= 1

    def pop(self):
        self.head = self.head.next
        self.length -= 1

    def _traverse(self, index):
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node.next
            counter += 1

        return current_node


if __name__ == '__main__':
    node = Node(3)

    assert node.value == 3
    assert node.next == None

    linked_list = LinkedList(node)

    assert len(linked_list) == 1
    assert linked_list.head == node
    assert linked_list.tail == node

    #Validating append behaviour
    # 3 (head) -> 5 (tail)

    linked_list.append(5)

    #Tail should be a new node
    assert linked_list.tail.value == 5
    assert linked_list.tail.next is None

    #Head still should keep track from node 5
    assert linked_list.head.value == 3
    assert linked_list.head.next.value == 5

    #should add one item to the LinkedList length
    assert len(linked_list) == 2

    #Validating prepend behaviour
    # 10(head) -> 3 -> 5 (tail)

    linked_list.prepend(10)

    #Head should be a new node but keep track from previous head
    assert linked_list.head.value == 10
    assert linked_list.head.next.value == 3
    assert linked_list.head.next.next.value == 5

    #should add one item to the LinkedList length
    assert len(linked_list) == 3

    # Validating insert behaviour

    linked_list.insert(
        index=1,
        value=15
    )

    assert repr(linked_list) == '< LinkedList 10 -> 15 -> 3 -> 5 -> None >'
    assert len(linked_list) == 4

    # Validating delete behaviour

    linked_list.remove(0)

    assert repr(linked_list) == '< LinkedList 15 -> 3 -> 5 -> None >'
    assert len(linked_list) == 3

    linked_list.remove(2)

    assert repr(linked_list) == '< LinkedList 15 -> 3 -> None >'
    assert len(linked_list) == 2
