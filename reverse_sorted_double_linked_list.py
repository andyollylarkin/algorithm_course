from operator import ne


class Node:
    def __init__(self, value=None, next_node=None):
        self.next_node = next_node
        self.value = value

    def __str__(self):
        return str(self.value)


class SortedList:
    def __init__(self, value=None, next_node=None):
        self.next_node = next_node
        self.value = value

        self.top = Node()
        self.bottom = Node(-1000)
        self.top.next_node = self.bottom

    def append(self, value):
        current = self.top
        new_node = Node(value)
        while current.next_node.value > value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node
            

    def __str__(self):
        current = self.top.next_node
        values = "["

        while current is not None and current.value > -1000:
            end = ", " if current.next_node and current.next_node.value > -1000 else ""
            values += str(current) + end
            current = current.next_node

        return values + "]"
