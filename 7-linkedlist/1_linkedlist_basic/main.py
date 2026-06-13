"""
LINKEDLIST 
Masih ingat bagaimana push method di queue mempunyai kompleksitas O(n) daripada  O(1)?
Contoh kodenya adalah seperti ini:
def push(self, item: str) -> None:
    # everything in self.items has to shift
    # up a position, which takes O(n) time
    self.items.insert(0, item)

Untuk membangun queue yang lebih cepat, kita menggunakan linked list daripada regular list (array).
Linked list adalah tipe data dimana elemen - elemennya tidak disimpan secara bersebelahan di memori,
melainkan setiap elemen merujuk ke elemen berikutnya.

NODES
Nodes direpresentasikan sebagai simple class dengan dua atribut yaitu value dan next.
- val: menyimpan nilai dari node tersebut
- next: menyimpan referensi ke node berikutnya dalam linked list
"""

"""
ASSIGNMENT
Let's lock-in and make LockedIn faster!
1. Complete the Node constructor.
    1. Set its val field to the provided value.
    2. Set its next field to None.
2. Complete the Node's set_next method. It should set the next field to the provided node.
"""

from typing import Any

class Node:
    def __init__(self, val: Any) -> None:
        self.val = val
        self.next = None

    def set_next(self, node: "Node") -> None:
        self.next = node

    # don't touch below this line

    def __repr__(self) -> str:
        return self.val
