# Design Dynamic Array (Resizable Array)
# Test Cases Cleared: 11/11
# Neetcode link: https://neetcode.io/problems/dynamicArray

class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [None] * capacity
        self.capacity = capacity
        self.length = 0

    
    def get(self, i: int) -> int:
        """Get value at a given index."""
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        """Set value at a given index."""
        self.array[i] = n


    def pushback(self, n: int) -> None:
        """Append value. Resize array if array is full."""
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1


    def popback(self) -> int:
        """Pop value."""
        if self.length > 0:
            pop_element = self.array[self.length - 1]
            self.length -= 1
            return pop_element

    def resize(self) -> None:
        """Resize array."""
        new_array = [None] * self.capacity * 2

        for index in range(self.length):
            new_array[index] = self.array[index]

        self.array = new_array
        self.capacity *= 2 


    def getSize(self) -> int:
        """Get array size."""
        return self.length
        
    
    def getCapacity(self) -> int:
        """Get array capacity."""
        return self.capacity
