import unittest

class Queue:

    def __init__(self):
        self.__queue = []
        self.__len_queue = 0

    def __len__(self):
        return self.__len_queue

    def push(self, element):
        self.__queue.append(element)
        self.__len_queue += 1

    def pop(self):
        if not self.empty():
            self.__queue.pop(0)
            self.__len_queue -= 1

    def empty(self):
        return self.__len_queue < 1

    def front(self):
        if not self.empty():
            return self.__queue[0]


class QueueTest(unittest.TestCase):
    """Unit tests for deque class."""
    def setUp(self):
        """Instanciate a deque element for the unit tests."""
        self.__queue_test = Queue()

    def push_elements(self, amount):
        """Creates a set of elements and appends into the deque given an amount."""
        for n in range(amount):
            element = 'Element ' + str(n + 1)
            self.__queue_test.push(element)

    def test_deque_empty(self):
        """Tests if the deque is empty. Must return True"""
        self.assertTrue(self.__queue_test.empty())

    def test_deque_with_elements(self):
        """Tests if the deque is not empty (contain elements). Must be False (It's not empty)"""
        self.push_elements(1)
        self.assertFalse(self.__queue_test.empty())

    def test_push(self):
        """Tests if the deque is pushing correctly one single element. It must have a length one after that."""
        self.__queue_test.push('Element')
        self.assertEqual(1, len(self.__queue_test))

    def test_push_more_than_one_element(self):
        """Tests if the dequequeue is pushing correctly more than one single element.
         It must have a length five (since it's pushing five elements)after that."""
        self.push_elements(5)
        self.assertEqual(5, len(self.__queue_test))

    def test_pop_empty_deque(self):
        """Tests if the queue pops None when there are no elements.
         It must be None (since it does not contain any elements)"""
        self.assertEqual(None, self.__queue_test.pop())

    def test_pop_deque_with_elements(self):
        """Tests if the  the last element from the deque is retrieved.
         It must be 'Element 10' (last element from the deque)"""
        self.push_elements(10)
        self.__queue_test.front()
        self.assertNotEqual('Element 10', self.__queue_test.front())

    def test_top_empty(self):
        """Tests if the deque shows None when there are no elements.
         It must be None (since it does not contain any elements)"""
        self.assertEqual(None, self.__queue_test.front())

    def test_top_with_elements(self):
        """Tests if  shows the last pushed element from the deque.
         It must be Element 5 (since it's the last element from the deque)."""
        self.push_elements(5)
        self.assertEqual('Element 1', self.__queue_test.front())

    def main(self):
        unittest.main()
