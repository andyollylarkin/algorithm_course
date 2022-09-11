class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

    def __str__(self):
        return "[" + ", ".join(map(str, self.data)) + "]"


class Stack(Array):
    def __init__(self, size):
        super().__init__(size)
        self.left_top = 0
        self.right_top = -1

    def pop_left(self):
        """
        Space complexity O(1)
        Time complexity O(1)
        """
        val = self.data[self.left_top]
        self.data[self.left_top] = None
        if self.left_top - 1 >= 0:
            self.left_top -= 1
        self.length -= 1
        return val

    def pop_right(self):
        """
        Space complexity O(1)
        Time complexity O(1)
        """
        val = self.data[self.right_top]
        self.data[self.right_top] = None
        if self.right_top + 1 <= -1:
            self.right_top += 1
        self.length -= 1
        return val

    def push_left(self, value):
        """
        Space complexity O(1)
        Time complexity O(1)
        """
        if self.length == self.size:
            raise OverflowError
        if self.data[self.left_top] is not None:
            self.left_top += 1
        self.data[self.left_top] = value
        self.length += 1

    def push_right(self, value):
        """
        Space complexity O(1)
        Time complexity O(1)
        """
        if self.length == self.size:
            raise OverflowError
        if self.data[self.right_top] is not None:
            self.right_top -= 1
        self.data[self.right_top] = value
        self.length += 1

    def clear(self):
        """ 
        Space complexity O(1)
        Time complexity O(n)
        """
        i = 0
        while i < self.size:
            self.data[i] = None
            i += 1
        self.length = 0
