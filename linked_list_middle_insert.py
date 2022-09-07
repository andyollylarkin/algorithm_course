class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


class List:

    def __init__(self):
        self.top = Node(None)

    def append(self, value):
        current = self.top
        while current.next_node is not None:
            current = current.next_node

        current.next_node = Node(value)

    def insert(self, value, after_value):
        current = self.top
        while current.next_node is not None:
            current = current.next_node
            if current.value == after_value:
                nxt = current.next_node
                current.next_node = Node(value)
                current.next_node.next_node = nxt
                return
        return
    def __str__(self):
        current = self.top.next_node
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"