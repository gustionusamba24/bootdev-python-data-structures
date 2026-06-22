from typing import Any


class Trie:
    def search_level(
        self, current_level: dict[str, Any], current_prefix: str, words: list[str]
    ) -> list[str]:
        if self.end_symbol in current_level:
            words.append(current_prefix)

        for letter in sorted(current_level.keys()):
            if letter != self.end_symbol:
                self.search_level(current_level[letter], current_prefix + letter, words)
                
        return words

    def words_with_prefix(self, prefix: str) -> list[str]:
        collected_words = []
        current_level = self.root
        for letter in prefix:
            if letter not in current_level:
                return []
            current_level = current_level[letter]
        return self.search_level(current_level, prefix, collected_words)

    # don't touch below this line

    def __init__(self) -> None:
        self.root = {}
        self.end_symbol = "*"

    def add(self, word: str) -> None:
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
        current_level[self.end_symbol] = True
