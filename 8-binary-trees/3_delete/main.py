"""
We also need a way to remove users from our BST if a user decides to delete their account.

ASSIGNMENT
Implement the recursive delete method. 
It takes a value as an input and deletes the node with that value if it exists. 
Each call returns the new root of the tree (or subtree) after the deletion.

Notice that in the test suite the delete method is called like this:
bst = bst.delete(character)

1. Check if the current node is empty (has no value). 
   If it is, return None. This represents an empty tree or a leaf node where deletion has already occurred.
2. If the value to delete is less than the current node's value:
    1. If there's a left child, 
       recursively delete the value from the left subtree and update the left child reference with the result.
    2. Return the current node.
3. If the value to delete is greater than the current node's value:
    1. If there's a right child, 
       recursively delete the value from the right subtree and update the right child reference with the result.
    2. Return the current node.
4. If the value to delete equals the current node's value, we've found the node to delete:
    1. If there is no right child, return the left child. This bypasses the current node, effectively deleting it.
    2. If there is no left child, return the right child, accomplishing the same thing.    
    3. If there are both left and right children:
        1. Start at the right child.
        2. Walk left until you find the smallest node in that right subtree. This is the next-largest value after the current node's value.
        3. Copy the next largest value into the current node's value.
        4. Delete the successor value from the right subtree by calling delete on it, and save the returned node as the new right child.
        5. Return the current node.
"""
from typing import Any


class BSTNode:
    def delete(self, val: Any) -> "BSTNode | None":
        if self.val is None:
            return None
        
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

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

    def get_min(self) -> Any:
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self) -> Any:
        current = self
        while current.right is not None:
            current = current.right
        return current.val
