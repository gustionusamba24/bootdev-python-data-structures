"""
ASSIGNMENT
Complete the add_to_tail method. It adds a new node to the end of the list and 
returns nothing.

1. If there isn't a head node, set the new node as the head.
2. Otherwise, keep a reference to the "last" node in the list - start with it set to the head.
3. Iterate over the linked list (you can use a for loop now that you've added your own __iter__ method)
    1. Update your "last" node reference to the current node
4. Once you've iterated over the entire list, you "last" reference should be the last node in the list(the tail).
   Set the next field of the "last" node to the new node.
"""


from node import Node


class LinkedList:
    def add_to_tail(self, node: Node) -> None:
        if self.head is None:
            self.head = node
        else:
            last = self.head

            for current in self:
                last = current

            last.set_next(node) 
        

    # don't touch below this line

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
