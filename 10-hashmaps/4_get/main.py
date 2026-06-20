from typing import Any


class HashMap:
    def get(self, key: str) -> Any:
        i = self.key_to_index(key)
        if self.hashmap[i] != None and self.hashmap[i][0] == key:
            return self.hashmap[i][1]
        else:
            raise Exception("sorry, key not found")
       

    # don't touch below this line

    def __init__(self, size: int) -> None:
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key: str) -> int:
        total = 0
        for c in key:
            total += ord(c)
        return total % len(self.hashmap)

    def insert(self, key: str, value: Any) -> None:
        i = self.key_to_index(key)
        self.hashmap[i] = (key, value)

    def __repr__(self) -> str:
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
