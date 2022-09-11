class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

    def __str__(self):
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


class Queue(Array):

    def __init__(self, size):
        super().__init__(size)
        self.first = 0
        self.length = 0

    def enqueue(self, value):
        """ Time complexity O(1); Space complexity O(1) """
        if self.length == self.size:
            raise OverflowError
        if self.data[0] is None:
            self.data[0] = value
            self.length += 1
            return
        self.data[self.length] = value
        self.length += 1

        

    def dequeue(self):
        """ Time complexity O(n); Space complexity O(1) """
        res = self.data[self.first]
        # If the first element is None , then there is no point in calculating
        if res is None:
            return None
        self.data[self.first] = None
        self.length -= 1
        idx = 0
        while idx < self.length:
            self.data[idx] = self.data[idx + 1]
            self.data[idx + 1] = None
            idx += 1
        return res