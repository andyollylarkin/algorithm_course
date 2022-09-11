class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


class Stack(Array):
    def __init__(self, size):
        super().__init__(size)
        self.top = -1

    def pop(self):
        if self.top >= 0:
            value = self.data[self.top]
            self.top -= 1
            self.length -= 1
            return value

    def push(self, value):
        if self.top + 1 == self.size:
            raise OverflowError
        self.top += 1
        self.length += 1
        self.data[self.top] = value

    def clear(self):
        i = 0
        length = self.length
        while i < length:
            self.data[i] = None
            self.length -= 1
            i += 1

    def peek(self):
        return self.data[self.top]

    def count(self):
        return self.length

# stack = Stack(3)
# stack.push(12)
# stack.push(7)
# stack.push(6)
# print(stack.peek()) #6
# print(stack.count()) #3
# stack.clear()
# print(stack.count()) #0
# print(stack.peek()) #None