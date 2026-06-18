"""
HEIGHT
Our DevOps team has been concerned with the hardware required to run 
the software using our BST. In an effort to diagnose the issue, 
they've asked us to write a method that returns the height of the tree. 
For example, this tree:
    5
   / \
  3   7
 /     \
1       9
has a height of 3, since the longest path from the root to a leaf is 5 -> 3 -> 1 or 5 -> 7 -> 9.
"""

"""
ASSIGNMENT
Complete the height method. It returns the height of the tree rooted at the current node.
1. If the node's value is None, return 0.
2. Recursively calculate the height of the left subtree.
3. Recursively calculate the height of the right subtree.
4. Use the max() function to return the maximum of the left and right subtree heights plus 1.
"""



from typing import Any


class BSTNode:
    def height(self) -> int:
        if self.val is None:
            return 0

        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0

        return max(left_height, right_height) + 1

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
