"""
ASSIGNMENT
Implement the add_to_head method. It should add a new node to the front of the list and return nothing.

1. Set the "next" field of the given node to the current head node.
2. Update the head reference to the given node.
"""


from node import Node


class LinkedList:
    def add_to_head(self, node: Node) -> None:
        node.set_next(self.head)
        self.head = node

    # don't touch below this line

    def add_to_tail(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            return
        last_node = self.head
        for current_node in self:
            last_node = current_node
        last_node.set_next(node)

    def __init__(self) -> None:
        self.head: Node | None = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
