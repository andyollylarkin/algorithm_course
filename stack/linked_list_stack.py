class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


class Stack:

    def __init__(self):
        self._top = Node(None)

    def pop(self):
        next: Node = self._top.next_node
        if next is None:
            return next
        self._top.next_node = next.next_node
        return next

    def push(self, value):
        node = Node(value)
        prev_top = self._top.next_node
        node.next_node = prev_top
        self._top.next_node = node