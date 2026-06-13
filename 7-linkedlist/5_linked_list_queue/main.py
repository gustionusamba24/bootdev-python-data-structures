"""
ASSIGNMENT

LockedIn's queue was working just fine on small datasets, 
but appending items once the list has 100,000+ items has started to take a toll on our servers. 
Implement these changes to speed up our Linked List's inserts to O(1):

1. Update the constructor to set self.tail to None.
2. Update add_to_head to also set the tail reference to the given node if the list is empty.
3. Update add_to_tail:
    1. Set the head and tail to the given node if the list is empty.
    2. Instead of iterating through the list to find the last node, 
       use the tail node to append the new node (for example, set self.tail.next to the new node).
    3. Update the tail reference to the new node.
"""


from node import Node


class LinkedList:
    def add_to_head(self, node: Node) -> None:
        if self.head is None:
            self.tail = node
        node.set_next(self.head)
        self.head = node

    def add_to_tail(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        self.tail.set_next(node)
        self.tail = node

    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    # don't touch below this line

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
