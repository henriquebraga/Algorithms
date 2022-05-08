class DynamicArray:
    
    def __init__(self, capacity=5):
        self.length = 0
        self.data = [None] * capacity
        self.capacity = capacity
    
    def append(self, el):
        if (self.length + 1 > self.capacity):
            self.resize()

        self.data[self.length] = el
        self.length += 1
        
    def pop(self):
        if self.length == 0:
            return None
        el = self.data[self.length - 1]

        self.data[self.length - 1] = None
        self.length -= 1

        return el
        
    def insert(self, el, index=0):
        if index < 0:
            index = 0
        if index >= self.length:
            index = self.length
        
        if (self.length + 1) > self.capacity:
            self.resize()
            
        for i in reversed(range(index, self.length)):
            self.data[i + 1] = self.data[i]
            
        self.data[index] = el
        self.length += 1
        
    def remove(self, index):
        if self.length == 0:
            return

        if index >= self.length - 1:
            self.pop()
            return

        if index < 0:
            index = 0
            
        for i in range(index + 1, self.length):
            self.data[i - 1] = self.data[i]
        
        self.data[self.length - 1] = None
        self.length -= 1

    def resize(self):
        self.capacity = self.capacity * 2
        resized_data = [None] * self.capacity
        
        for i, el in enumerate(self.data):
            resized_data[i] = el
            
        self.data = resized_data

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        
        if self.length == 0:
            return None
    
        if index > (self.length - 1):
            return self.data[self.length - 1]

        if index <= 0:
            return self.data[0]

        return self.data[index]


if __name__ == '__main__':

    dynamic_array = DynamicArray()

    #Should create initial state
    assert len(dynamic_array) == 0
    assert dynamic_array.data == [None, None, None, None, None]
    assert dynamic_array.capacity == 5


    #should return None when no element in dynamic array

    assert dynamic_array[100] is None

    #should append

    dynamic_array.append(10)

    assert len(dynamic_array) == 1
    assert dynamic_array.data == [10, None, None, None, None]


    #should get first item when negative

    assert dynamic_array[-1] == 10

    #should get first item when zero
    assert dynamic_array[0] == 10

    assert dynamic_array[5] == 10


    #should resize when bigger than capacity

    dynamic_array.append(23)
    dynamic_array.append(44)
    dynamic_array.append(11)
    dynamic_array.append(32)
    dynamic_array.append(1)

    assert len(dynamic_array) == 6
    assert dynamic_array.capacity == 10
    assert dynamic_array.data == [10, 23, 44, 11, 32, 1, None, None, None, None]

    #pop should return None when dynamic array is empty
    empty_dynamic_array = DynamicArray()

    assert len(empty_dynamic_array) == 0
    assert empty_dynamic_array.pop() is None

    #pop should return last element from dynamic array
    assert len(dynamic_array) == 6

    popped = dynamic_array.pop()

    assert popped == 1
    assert len(dynamic_array) == 5
    assert dynamic_array.data == [10, 23, 44, 11, 32, None, None, None, None, None]

    #should insert in the beginning when no index is passed
    dynamic_array.insert(431)

    assert len(dynamic_array) == 6
    assert dynamic_array[0] == 431
    assert dynamic_array.data == [431, 10, 23, 44, 11, 32, None, None, None, None]

    #should insert in the beginning when no index is negative
    dynamic_array.insert(100, index=-1)

    assert len(dynamic_array) == 7
    assert dynamic_array[0] == 100
    assert dynamic_array.data == [100, 431, 10, 23, 44, 11, 32, None, None, None]

    #should insert in the position in index parameter

    dynamic_array.insert(29, index=3)

    assert len(dynamic_array) == 8
    assert dynamic_array[3] == 29
    assert dynamic_array.data == [100, 431, 10, 29, 23, 44, 11, 32, None, None]

    dynamic_array.insert(902, index=1)

    assert len(dynamic_array) == 9
    assert dynamic_array[1] == 902
    assert dynamic_array.data == [100, 902, 431, 10, 29, 23, 44, 11, 32, None]

    dynamic_array.insert(451, index=7)

    assert len(dynamic_array) == 10
    assert dynamic_array[7] == 451
    assert dynamic_array.data == [100, 902, 431, 10, 29, 23, 44, 451, 11, 32]

    #should resize when is above capacity

    dynamic_array.insert(1, index=100)
    assert len(dynamic_array) == 11
    assert dynamic_array.capacity == 20
    assert dynamic_array[10] == 1
    assert dynamic_array.data == [100, 902, 431, 10, 29, 23, 44, 451, 11, 32, 1, None, None, None, None, None, None, None, None, None]


    #remove should pop when index is equal to last or bigger


    #removing last element when index passed is equal/bigger length (element 1 at index 10)
    dynamic_array.remove(100)

    assert len(dynamic_array) == 10
    assert dynamic_array.data == [100, 902, 431, 10, 29, 23, 44, 451, 11, 32, None, None, None, None, None, None, None, None, None, None]

    #removing last element index (32 at index 9)
    dynamic_array.remove(9)

    assert len(dynamic_array) == 9

    assert dynamic_array.data == [100, 902, 431, 10, 29, 23, 44, 451, 11, None, None, None, None, None, None, None, None, None, None, None]


    #removing first element index when passing negative index (100 at index 0)
    dynamic_array.remove(-1)

    assert len(dynamic_array) == 8

    assert dynamic_array[0] != 100

    assert dynamic_array.data == [902, 431, 10, 29, 23, 44, 451, 11, None, None, None, None, None, None, None, None, None, None, None, None]

    #removing second element index when passing 2 index (431 at index 1)

    dynamic_array.remove(1)

    assert len(dynamic_array) == 7
    assert dynamic_array.data == [902, 10, 29, 23, 44, 451, 11, None, None, None, None, None, None, None, None, None, None, None, None, None]
