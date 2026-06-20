from typing import Any


class HashMap:
    def key_to_index(self, key: str) -> int:
        return sum([ord(c) for c in key]) % len(self.hashmap)

    # don't touch below this line

    def __init__(self, size: int) -> None:
        self.hashmap = [None for i in range(size)]

    def __repr__(self) -> str:
        buckets = []
        for v in self.hashmap:
            if v != None:
                buckets.append(v)
        return str(buckets)

# Just for testing the key_to_index function, you can ignore this part.
def key_to_index(key: str):
    return sum([ord(c) for c in key]) % 10

print(key_to_index("Blake#0"))