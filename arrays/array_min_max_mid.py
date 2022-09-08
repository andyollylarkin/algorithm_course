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

    def min(self):
        min = self.data[0]
        for i in self.data:
            if i is None:
                return min
            if i < min and i is not None:
                min = i
        return min

    def max(self):
        max = self.data[0]
        for i in self.data:
            if i is None:
                return max
            if i > max and i is not None:
                max = i
        return max

    def avg(self):
        sum = 0
        for i in self.data:
            if i is None:
                break
            sum += i
        return sum / self.length

    def __str__(self):
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"