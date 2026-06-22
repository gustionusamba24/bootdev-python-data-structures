from typing import Any


class Trie:
    def longest_common_prefix(self) -> str:
        current = self.root
        prefix = ""
        while True:
            children = []
            for key in current.keys():
                if key != self.end_symbol:
                    children.append(key)
            if self.end_symbol in current or len(children) != 1:
                break
            prefix += children[0]
            current = current[children[0]]
        return prefix

    # don't touch below this line

    def __init__(self) -> None:
        self.root = {}
        self.end_symbol = "*"

    def add(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True
