"""
It's called a "stack" because it behaves just like a stack of physical items. 
Imagine a stack of plates: it's easy to take an item off the top of the stack, 
but you can't really get to the items in the middle or at the bottom without 
removing the items on top first. You'll often hear a stack 
referred to as a LIFO (last in, first out) data structure.
"""


from typing import Any

class Stack:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def push(self, item: Any) -> None:
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)