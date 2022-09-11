from operator import length_hint


class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

    def __str__(self):
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


class Stack(Array):
    def __init__(self, size):
        super().__init__(size)

    def pop(self):
        val = self.data[self.length - 1]
        self.data[self.length - 1] = None
        self.length -= 1
        return val

    def push(self, value):
        if self.length == self.size:
            raise OverflowError
        self.data[self.length] = value
        self.length += 1