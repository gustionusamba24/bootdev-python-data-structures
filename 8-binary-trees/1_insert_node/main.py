"""
THE IMPLEMENTATION OF BINARY SEARCH TREE IN LOCKEDIN
Throughout this chapter we'll be building a binary search tree to power LockedIn's custom database. 
LockedIn's management doesn't trust so called "open-source"... so here we are. 
One of the primary features of databases is the ability to look up records by a single key,
and binary search trees are the most common way to implement these fast lookups.

Each node in our BST will represent a LockedIn user. A BSTNode has three properties:

- value: The value of the node, a User object in our case (see user.py). 
  You'll notice that Users have a name and an ID. Comparison operators are already 
  implemented for you on the class, so you should be able to compare User objects with ==, <, and > directly. 
  The ID is the value that we'll use to determine the order of the nodes in the tree.
- left: The left child of the node, another BSTNode or None.
- right: The right child of the node, another BSTNode or None.
"""

"""
ASSIGNMENT
Complete the insert method of the BSTNode class. 
It takes a User object as input and adds it to a new node if the value doesn't already exist in the tree.

1. If the node doesn't have a value yet, store the given value and return
2. If the node's value is equal to the given value, just return, no duplicates allowed
3. If the given value is less than the node's value and the node doesn't have a left child, 
   create a new left child node with the given value and return
4. If the given value is less than the node's value and the node does have a left child, 
   recursively call insert off of that left child with the given value and return
5. Since we already checked if the given value is equal to or less than the node, 
   the value must be greater than the node. Handle whether or not the node already has a right child
"""

"""
TIP
I'd highly recommend using pencil/paper or some kind of drawing tool to visualize 
the tree as you go through the assignments in this chapter.
"""


from typing import Any


class BSTNode:
    def __init__(self, val: Any = None) -> None:
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None
        self.val = val

    def insert(self, val: Any) -> None:
        if self.val is None:
            self.val = val
            return

        if val == self.val:
            return

        if val < self.val:
            if self.left is None:
                self.left = BSTNode(val)
                return
            else:
                self.left.insert(val)
                return

        if val > self.val:
            if self.right is None:
                self.right = BSTNode(val)
                return
            else:
                self.right.insert(val)
                return
