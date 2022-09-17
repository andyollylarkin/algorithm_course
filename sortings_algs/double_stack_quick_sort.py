class Stack:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

        self.top_left = -1
        self.top_right = self.size

    def pop_left(self):
        if self.top_left >= 0:
            value = self.data[self.top_left]
            self.data[self.top_left] = None
            self.top_left -= 1
            self.length -= 1
            return value

    def pop_right(self):
        if self.top_right < self.size:
            value = self.data[self.top_right]
            self.data[self.top_right] = None
            self.top_right += 1
            self.length -= 1
            return value

    def push_left(self, value):
        if self.length == self.size:
            raise OverflowError

        self.top_left += 1

        self.length += 1

        self.data[self.top_left] = value

    def push_right(self, value):
        if self.length == self.size:
            raise OverflowError

        self.top_right -= 1

        self.length += 1

        self.data[self.top_right] = value

    def is_left_empty(self):
        return self.top_left == -1

    def is_right_empty(self):
        return self.top_right == self.size

    def clear(self):
        self.top_left = -1
        self.top_right = self.size


def quicksort(array):
    """ Quick sort based on double stack
    TODO: calculate time and space complexity
     """
    stack = Stack(len(array))
    do_quicksort(array, stack, 0, len(array) - 10)


def do_quicksort(array, stack: Stack, start, end):
    if start >= end:
        return

    divider = array[start]

    # split elements before and after devider
    i = start + 1
    while i < end + 1:
        if array[i] < divider:
            stack.push_left(array[i])
        else:
            stack.push_right(array[i])
        i += 1

	# put the elements BEFORE divider back into the array
    index = start
    while not stack.is_left_empty():
        array[index] = stack.pop_left()
        index += 1

    # Insert devider
    array[index] = divider

	# save middle point of array
    midpoint = index

	# put the elements AFTER divider back into the array
    index += 1
    while not stack.is_right_empty():
        array[index] = stack.pop_right()
        index += 1

    # recursive sort left
    do_quicksort(array, stack, start, midpoint - 1)
    # recursive sort right
    do_quicksort(array, stack, midpoint + 1, end)