# Fix Insert
Rotations are only useful if we can use them. When new nodes are inserted into the tree, they can break the red-black properties. We'll fix that by rotating the tree as new nodes are inserted, ensuring the tree remains balanced.

When we're done here, we will have a fully functional (albeit insert-only) red-black tree. As you can see if you look at the bottom of the test suite, we'll be inserting numbers into our tree in order. A normal binary tree would break down into a single unruly branch:
```                  
                  > 7
               > 6
            > 5
         > 4
      > 3
   > 2
> 1
```

But our red-black tree will remain balanced:
```
      > 7
   > 6
      > 5
> 4
      > 3
   > 2
      > 1
```

## Assignment
In our implementation, we'll perform a "normal" insert, and then call a fix_insert method that will recolor and rotate the tree as necessary. This will ensure that the red-black properties are maintained.
1. Complete the insert method to call our balancing method after inserting a new node.
2. Complete the fix_insert method that maintains red-black tree properties, starting with the newly inserted node as the current node:
    1. While the current node is not the root and has a red parent:
        1. Identify the parent and grandparent nodes of the current node
        2. If the parent is a right child of the grandparent:
            1. Identify the uncle node (the grandparent's left child)
            2. If the uncle is red:
                - Recolor the uncle and parent to black
                - Recolor the grandparent to red
                - Move up the tree by making the current node the grandparent
            3. If the uncle is black:
                - If the current node is the left child of the parent:
                    - Move up the tree by making the current node the parent
                    - Call rotate_right with the current node as the pivot_parent
                    - Set the parent to be the current node's parent
                - Recolor the parent to black
                - Recolor the grandparent to red
                - Call rotate_left with the grandparent as the pivot_parent
        3. If the parent is a left child of the grandparent:
            1. Identify the uncle node (the grandparent's right child)
            2. If the uncle is red:
                - Recolor the uncle and parent to black
                - Recolor the grandparent to red
                - Move up the tree by making the current node the grandparent
            3. If the uncle is black:
                - If the current node is the right child of the parent:
                    - Move up the tree by making the current node the parent
                    - Call rotate_left with the current node as the pivot_parent
                    - Set the parent to be the current node's parent
                - Recolor the parent to black
                - Recolor the grandparent to red
                - Call rotate_right with the grandparent as the pivot_parent
    2. Recolor the root to black