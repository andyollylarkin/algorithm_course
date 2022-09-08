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

    def remove(self, value):
        i = 0
        idx = None
        while i < self.length:
            if self.data[i] == value:
                idx = i
                self.data[i] = None
                break
            i += 1
        # if element was found, shift all element to right
        if idx is not None:
            while idx < self.length - 1:
                self.data[idx] = self.data[idx+1]
                idx += 1
            self.data[self.length - 1] = None
            self.length -= 1

    def __str__(self):
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"
