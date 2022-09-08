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

    def __str__(self):
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"