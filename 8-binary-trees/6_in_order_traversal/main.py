"""
INORDER  TRAVERSAL
An "inorder" traversal is the most intuitive way to visit all the nodes in a tree. 
It's called "inorder" because the current node is visited between its children. 
It results in an ordered list of the nodes in the tree.
"""

"""
ASSIGNMENT
Turns out, the data team had no idea what they were talking about, 
and our product lead just wanted an export of our tree in sorted order. 
He wants to be able to see the users in the order they signed up (and were thus given user IDs).

Implement the recursive inorder method. Here are the algorithm's steps:
1. Recursively traverse the left subtree.
2. Visit the value of the current node by appending its value to the visited array.
3. Recursively traverse the right subtree.
4. Return the list of nodes visited so far.
"""

from typing import Any


class BSTNode:
    def inorder(self, visited: list[Any]) -> list[Any]:
        if self.left is not None:
            self.left.inorder(visited)
        visited.append(self.val)
        if self.right is not None:
            self.right.inorder(visited)
        return visited

    # don't touch below this line

    def __init__(self, val: Any = None) -> None:
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None
        self.val = val

    def insert(self, val: Any) -> None:
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
