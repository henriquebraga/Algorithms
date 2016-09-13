import unittest
class Stack:
    """Example of a stack structure (FILO - First in, Last out)."""

    def __init__(self):
        self.__items = []

    def push(self, element):
        """Inserts at the top of the stack."""
        self.__items.append(element)

    def pop(self):
        """Pop the last element from the stack. (if there is any)"""
        if not self.empty():
            self.__items.pop()

    def top(self):
        """Retrieves the top (last pushed element) from the stack, but it does not pop it.
          When the stack does not contain any elements, it retrieves None.
         """
        if not self.empty():
            return self.__items[-1]

    def empty(self):
        """ Says whether the stack is empty or not. (True if it's empty)
         """
        return not self.__items

    def __len__(self):
        return len(self.__items)


class StackTest(unittest.TestCase):
    """Unit tests for Stack class."""
    def setUp(self):
        """Instanciate a stack element for the unit tests."""
        self.__stack_test = Stack()

    def push_elements(self, amount):
        """Creates a set of elements and appends into the stack given an amount."""
        for n in range(amount):
            element = 'Element ' + str(n + 1)
            self.__stack_test.push(element)

    def test_stack_empty(self):
        """Tests if the stack is empty. Must return True"""
        self.assertTrue(self.__stack_test.empty())

    def test_stack_with_elements(self):
        """Tests if the stack is not empty (contain elements). Must be False (It's not empty)"""
        self.push_elements(1)
        self.assertFalse(self.__stack_test.empty())

    def test_push(self):
        """Tests if the stack is pushing correctly one single element. It must have a length one after that."""
        self.__stack_test.push('Element')
        self.assertEqual(1, len(self.__stack_test))

    def test_push_more_than_one_element(self):
        """Tests if the stack is pushing correctly more than one single element.
         It must have a length five (since it's pushing five elements)after that."""
        self.push_elements(5)
        self.assertEqual(5, len(self.__stack_test))

    def test_pop_empty_stack(self):
        """Tests if the stack pops None when there are no elements.
         It must be None (since it does not contain any elements)"""
        self.assertEqual(None, self.__stack_test.pop())

    def test_pop_stack_with_elements(self):
        """Tests if the  the last element from the stack is retrieved.
         It must be 'Element 10' (last element from the stack)"""
        self.push_elements(10)
        self.__stack_test.pop()
        self.assertNotEqual('Element 10', self.__stack_test.top())

    def test_top_empty(self):
        """Tests if the stack shows None when there are no elements.
         It must be None (since it does not contain any elements)"""
        self.assertEqual(None, self.__stack_test.top())

    def test_top_with_elements(self):
        """Tests if  shows the last pushed element from the stack.
         It must be Element 5 (since it's the last element from the stack)."""
        self.push_elements(5)
        self.assertEqual('Element 5', self.__stack_test.top())

    def main(self):
        unittest.main()

