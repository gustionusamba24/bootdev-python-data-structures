"""
POSTORDER TRAVERSAL
A "postorder" traversal also visits all the nodes in a tree. 
It's called "postorder" because the current node is visited after its children.
"""

"""
ASSIGNMENT
Our data team didn't like the way we ordered the users in our 
BST export (personally I think they just want to kick the work for themselves down the road). 
Anyhow, we've been asked to change it.
Implement the recursive postorder method. Here are the algorithm's steps:
1. Recursively traverse the left subtree
2. Recursively traverse the right subtree
3. Visit the value of the current node by appending its value to the visited array
4. Return array of visited nodes
"""


from typing import Any


class BSTNode:
    def postorder(self, visited: list[Any]) -> list[Any]:
        if self.left is not None:
            self.left.postorder(visited)
        if self.right is not None:
            self.right.postorder(visited)
        if self.val is not None:
            visited.append(self.val)
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
