"""
ASSIGNMENT
The LinkedList class is a wrapper class that uses the Node class we already wrote

1. Complete the __init__ method. It should set the head field to None.
No other node points to the linked list's head (first) node, 
so the LinkedList class itself needs to keep track of it. We'll use the term head and tail like this:
"`head node` -> `node` -> `node` -> `node` -> `tail node`"

2. Complete the __iter__ method. It should be a generator function that 
   yields each node in the linked list, from the head to the tail.
   1. Create a reference to the head node (e.g. node = self.head)
   2. Use a while loop to iterate over the linked list until node is None
        1. Yield the current node
        2. Set node to the next node
"""


from node import Node


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # don't touch below this line

    def __repr__(self) -> str:
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)