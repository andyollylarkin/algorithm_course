class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def __str__(self):
        return str(self.value)


class Queue:
    def __init__(self):
        self.top: Node = Node(None)
        self.first: Node = None

    def enqueue(self, value):
        """ Space complexity O(1); Time complexity O(1) """
        new_node = Node(value)
        if self.top.next_node is None:
            new_node.prev_node = self.top
            self.top.next_node = new_node
            self.first = self.top.next_node
            return
        new_node.prev_node = self.top
        new_node.next_node = self.top.next_node
        self.top.next_node.prev_node = new_node
        self.top.next_node = new_node

    def dequeue(self):
        """ Space complexity O(1); Time complexity O(1) """
        # if queue is empty return none
        if self.first.value is None:
            return None
        res = self.first
        self.first = self.first.prev_node
        self.first.next_node = None
        return res.value