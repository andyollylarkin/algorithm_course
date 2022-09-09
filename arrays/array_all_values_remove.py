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
        elementDeleted = 0
        i = 0
        # Mark founded element as None
        while i < self.length:
            if self.data[i] == value:
                self.data[i] = None
                elementDeleted += 1
                i += 1
            else:
                i+= 1
        i = 0
        # shift all element to left
        while i < self.length - 1:
            if self.data[i] is None:
                if self.data[i + 1] is None:
                    i += 1
                    continue
                self.data[i] = self.data[i+1]
                self.data[i + 1] = None
                i = 0
            else:
                i += 1
        self.length -= elementDeleted
        
            

    def __str__(self):
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"