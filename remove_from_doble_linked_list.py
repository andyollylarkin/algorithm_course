class Node:
    def __init__(self, value=None, next_node=None, prev_node=None):
        self.next_node = next_node
        self.prev_node = prev_node
        self.value = value

    def __str__(self):
        return str(self.value)


class List:
    def __init__(self):

        self.top = Node()

    def append(self, value):
        current = self.top
        while current.next_node is not None:
            current = current.next_node

        new_node = Node(value)
        current.next_node = new_node
        new_node.prev_node = current

    def remove(self, value):
        current = self.top
        while current.next_node is not None:
            current = current.next_node
            if(current.value == value):
                if current.next_node is not None:
                    current.next_node.prev_node = current.prev_node or None
                if current.prev_node is not None:
                    current.prev_node.next_node = current.next_node or None
                return

    def __str__(self):
        current = self.top.next_node
        values = "["

        while current is not None:
            end = ", " if current.next_node else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"