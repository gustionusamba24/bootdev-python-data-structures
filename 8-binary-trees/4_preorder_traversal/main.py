"""
PREORDER TRAVERSAL
A "preorder" traversal is a way to visit all the nodes in a tree. 
It's called "preorder" because the current node is visited before its children.

Sometimes it's useful (albeit a bit slow) to iterate over all the nodes in the tree. 
In the case of LockedIn, 
we've been asked to build a way to create a backup of our database indexes 
- this traversal will allow us to save all the data in the tree to a file.
"""

"""
ASSIGNMENT
Implement the recursive preorder method. 
It returns a list of the values in the order they are visited, 
and it takes as an argument the ordering of values we have visited so far.

For example, the first call to preorder on an entire tree would be:
# an empty list is passed in the first call
bst_node.preorder([])

Here are the algorithm's steps:
1. If the current node actually contains a value (self.val is not None), 
   visit it by appending its value to the visited array
2. Recursively traverse the left subtree
3. Recursively traverse the right subtree
4. Return the array of visited nodes
"""


from typing import Any


class BSTNode:
    def preorder(self, visited: list[Any]) -> list[Any]:
        if self.val is not None:
            visited.append(self.val)
        if self.left:
            self.left.preorder(visited)
        if self.right:
            self.right.preorder(visited)
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
