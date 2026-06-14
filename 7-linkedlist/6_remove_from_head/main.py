"""
REMOVE FROM HEAD
We're one method away from having a fully functioning O(1) Queue! 
We just need a way to remove the first element from the linked list in constant time. 
When we're finished, our LinkedList will fulfill the basic requirements of a Queue:
1. add_to_tail: Constant time insert
2. remove_from_head: Constant time pop

Let's rename the LinkedList class to LLQueue and remove the add_to_head 
functionality because Queues don't allow inserting into the wrong end.

We've also flipped the arrows in the printed representation to reflect the change.
"""

"""
ASSIGNMENT
Complete the remove_from_head method. 
It should remove the first node from the list (the head) and return it.
1. If the list is empty, just return None.
2. Assign the head to be removed to a variable.
3. Set the list's head to the next node in the list.
4. If the list became empty, set the list's tail to None.
5. Set the (now removed) head's next to None. We don't want it to point to any node in the list.
6. Return the removed head.
"""
from node import Node


class LLQueue:
    def remove_from_head(self) -> Node | None:
        if self.head is None:
            return None
        removed_head = self.head
        self.head = removed_head.next
        if self.head is None:
            self.tail = None
        removed_head.next = None
        return removed_head

    # don't touch below this line

    def add_to_tail(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.set_next(node)
        self.tail = node

    def __init__(self) -> None:
        self.tail: Node | None = None
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
        return " <- ".join(nodes)
