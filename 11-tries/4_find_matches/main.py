from typing import Any


class Trie:
    def find_matches(self, document: str) -> set[str]:
        matched_words = set()
        for i in range(len(document)):
            current_level = self.root
            for j in range(i, len(document)):
                letter = document[j]
                if letter not in current_level:
                    break
                current_level = current_level[letter]
                if self.end_symbol in current_level:
                    matched_words.add(document[i : j + 1])
        return matched_words
                

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
