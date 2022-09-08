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

    def insert(self, index, value):
        if self.length == self.size:
            raise OverflowError
        if index >= self.length:
            self.append(value)
            return
        slice = self.data[index:self.length] # save elements to be moved
        for i in range(index + 1, self.length + 1): # from the next element to the number of current elements
            if i >= self.size: # if insert can got out of bounds
                raise OverflowError
            self.data[i] = slice[0]
            del slice[0]
        self.data[index] = value
        self.length += 1

    def __str__(self):
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"
