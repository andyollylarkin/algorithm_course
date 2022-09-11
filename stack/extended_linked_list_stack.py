class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return str(self.value)


class Stack:
    def __init__(self):
        self.top = Node(None)
        self.count_items = 0

    def pop(self):
        top = self.top.next_node

        if top:
            self.top.next_node = top.next_node
            return top.value

    def push(self, value):
        new_node = Node(value)
        new_node.next_node = self.top.next_node
        self.top.next_node = new_node
        self.count_items += 1

    def clear(self):
        """
        Time complexity O(n)
        Space complexity O(1)
        """
        current = self.top.next_node
        while current.next_node is not None:
            if current.next_node is not None:
                # Make the top of the stack is's next value
                self.top.next_node = current.next_node 
                current = current.next_node
                self.count_items -= 1
        # remove last stack element
        self.top.next_node = None
        self.count_items -= 1
        

    def peek(self):
        return self.top.next_node.value if self.top.next_node is not None else None

    def count(self):
        return self.count_items