class DynamicArray:

    def __init__(self, capacity :int = 10):
        self.length = 0
        self.capacity = capacity
        self.data = {}

    def append(self, value: int) -> None:
        if (self.length + 1) > self.capacity:
            self._resize_data()

        self.data[self.length] = value
        self.length += 1

    def pop(self) -> int:
        element = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1

        return element

    def insert(self, value: int, index: int=None):
        if index is None:
            return self.append(value)

        if (self.length + 1) > self.capacity:
            self._resize_data()

        for i in reversed(range(index, self.length)): #giving room for the new number to be inserted (moving them to the right)
            self.data[i + 1] = self.data[i]

        self.data[index] = value
        self.length += 1

    def remove(self, index: int):
        #1,2,3,4,5
        for i in range(index + 1, self.length): #move items to right
            self.data[i - 1] = self.data[i]

        del self.data[self.length - 1]
        self.length -= 1

    def _resize_data(self):
        self.capacity += 10
        new_data = {i: v for i, v in self.data.items()} # just a simulation how we would resize an array
        self.data = new_data

    def __getitem__(self, index) -> int:
        return self.data.get(index)

    def __len__(self):
        return self.length


if __name__ == '__main__':
    dynamic_array = DynamicArray(capacity=3)

    assert dynamic_array.length == 0
    assert dynamic_array.capacity == 3
    assert dynamic_array.data == {}

    assert dynamic_array[0] is None

    #append behavior should add at the end of the list
    dynamic_array.append(10)

    assert dynamic_array[0] == 10
    assert len(dynamic_array) == 1

    #append behavior should increase capacity when exceeds configured capacity

    dynamic_array.append(20)
    dynamic_array.append(30)

    #now it will overflow array's capacity
    dynamic_array.append(40)

    assert len(dynamic_array) == 4
    assert dynamic_array.capacity == 13

    assert dynamic_array[0] == 10
    assert dynamic_array[1] == 20
    assert dynamic_array[2] == 30
    assert dynamic_array[3] == 40

    #pop behavior: should return and remove last item inserted from array

    assert dynamic_array.pop() == 40
    assert len(dynamic_array) == 3
    assert dynamic_array[2] == 30

    #insert behavior: should append (add at the end of the array) if no index is provided
    dynamic_array.insert(40)

    assert len(dynamic_array) == 4
    assert dynamic_array[3] == 40

    #insert behavior: should insert in index position
    dynamic_array.insert(value=25, index=2)

    assert len(dynamic_array) == 5

    assert dynamic_array[0] == 10
    assert dynamic_array[1] == 20
    assert dynamic_array[2] == 25
    assert dynamic_array[3] == 30
    assert dynamic_array[4] == 40

    #remove behavior: should remove element at index position
    #10,20,30,40
    dynamic_array.remove(2)

    assert len(dynamic_array) == 4

    assert dynamic_array[0] == 10
    assert dynamic_array[1] == 20
    assert dynamic_array[2] == 30
    assert dynamic_array[3] == 40
