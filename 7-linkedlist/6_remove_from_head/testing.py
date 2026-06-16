from main import LLQueue
from node import Node

ll = LLQueue()
print(f"Current LLQueue: {ll}")

n1 = Node("A")
n2 = Node("B")
n3 = Node("C")

print(f"Adding {n1} to tail")
ll.add_to_tail(n1)
print(f"Current LLQueue: {ll}")
print(f"Adding {n2} to tail")
ll.add_to_tail(n2)
print(f"Current LLQueue: {ll}")
print(f"Adding {n3} to tail")
ll.add_to_tail(n3)
print(f"Current LLQueue: {ll}")

print()

print(f"Removing from head: {ll.remove_from_head()}")
print(f"Current LLQueue: {ll}")
print(f"Removing from head: {ll.remove_from_head()}")
print(f"Current LLQueue: {ll}")
print(f"Removing from head: {ll.remove_from_head()}")
print(f"Current LLQueue: {ll}")