from typing import Any


class HashMap:
    def insert(self, key: str, value: Any) -> None:
        # ?
        self.resize()
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self) -> None:
        if len(self.hashmap) == 0:
            self.hashmap.append(None)
            return

        if self.current_load() < 0.05:
            return

        temp_hashmap = self.hashmap
        self.hashmap = [None for i in range(len(temp_hashmap) * 10)]
        for v in temp_hashmap:
            if v != None:
                self.insert(v[0], v[1])

    def current_load(self) -> float:
        if len(self.hashmap) == 0:
            return 1
        
        filled_buckets = 0
        for v in self.hashmap:
            if v != None:
                filled_buckets += 1
        return filled_buckets / len(self.hashmap)
        

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
