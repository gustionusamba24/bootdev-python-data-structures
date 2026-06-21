from typing import Any


class HashMap:
    def insert(self, key: str, value: Any) -> None:
        original_index = self.key_to_index(key)
        first_iteration = True
        while self.hashmap[original_index] != None and self.hashmap[original_index][0] != key:
            if not first_iteration and self.key_to_index(key) == original_index:
                raise Exception("hashmap is full")
            original_index = (original_index + 1) % len(self.hashmap)
            first_iteration = False
        self.hashmap[original_index] = (key, value)

    def get(self, key: str) -> Any:
        original_index = self.key_to_index(key)
        first_iteration = True
        while self.hashmap[original_index] != None:
            if self.hashmap[original_index][0] == key:
                return self.hashmap[original_index][1]
            if not first_iteration and self.key_to_index(key) == original_index:
                raise Exception("sorry, key not found")
            original_index = (original_index + 1) % len(self.hashmap)
            first_iteration = False
        raise Exception("sorry, key not found")

    # don't touch below this line

    def __init__(self, size: int) -> None:
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key: str) -> int:
        total = 0
        for c in key:
            total += ord(c)
        return total % len(self.hashmap)

    def __repr__(self) -> str:
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
