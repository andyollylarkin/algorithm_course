class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

    def append(self, value):
        if self.length == self.size:
            raise OverflowError
        self.data[self.length] = value
        self.length += 1

    def reverse(self):
        """
        Two pointers method
        """
        right = 0
        left = self.length - 1
        while right < left:
            self.data[right], self.data[left] = self.data[left], self.data[right]
            right += 1
            left -= 1


    def __str__(self):
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


array = Array(9)
array.append(6)
array.append(2)
array.append(1)
array.append(9)
array.append(10)
array.append(11)
array.append(14)
array.append(8)
array.append(7)
print(array)
array.reverse()
print(array)