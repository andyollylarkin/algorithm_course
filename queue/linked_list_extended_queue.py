class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __str__(self):
        return self.value


class Queue:
    def __init__(self, size):
        self.top = Node(None)
        self.first = None
        self.size = size
        self.length = 0

    def enqueue(self, value):
        """ Time complexity O(1); Space complexity O(1) """
        if self.length == self.size:
            raise OverflowError
        new_node = Node(value)
        if self.top.next_node:
            self.top.next_node.prev_node = new_node

        new_node.next_node = self.top.next_node
        new_node.prev_node = self.top
        self.top.next_node = new_node

        if not self.first:
            self.first = new_node
        self.length += 1

    def dequeue(self):
        """ Time complexity O(1); Space complexity O(1) """
        if self.first:
            value = self.first.value

            self.first = self.first.prev_node

            self.first.next_node = None

            if self.first.value is None:
                self.first = None

            self.length -= 1
            return value

        return None

    def count(self):
        """ Time complexity O(1); Space complexity O(1) """
        return self.length

    def peek(self):
        """ Time complexity O(1); Space complexity O(1) """
        if self.first == None:
            return None
        return self.first.value

    def clear(self):
        """ Time complexity O(1); Space complexity O(1) """
        self.first = None
        self.length = 0
        self.top.next_node = None