import json
from typing import Any


class Trie:
    def exists(self, word: str) -> bool:
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return self.end_symbol in current

    # don't touch below this line

    def add(self, word: str) -> None:
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def __init__(self) -> None:
        self.root = {}
        self.end_symbol = "*"

    def __str__(self) -> str:
        return json.dumps(self.root, sort_keys=True, indent=4)


if __name__ == "__main__":
    term_in_tech: list[str] = ["dev", "devops", "devs"]
    trie = Trie()
    for word in term_in_tech:
        trie.add(word)
    print(trie)