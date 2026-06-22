import json
from typing import Any


class TrieVisualization:
    def add_with_steps(self, word: str) -> None:
        """Menambahkan kata ke trie dengan visualisasi step by step"""
        current = self.root
        print(f"\n{'='*60}")
        print(f"Menambahkan kata: '{word}'")
        print(f"{'='*60}")
        
        for step, letter in enumerate(word, 1):
            print(f"\n--- STEP {step}: Memproses karakter '{letter}' ---")
            print(f"Current node sebelum: {current}")
            
            # Cek apakah karakter sudah ada di node saat ini
            if letter not in current:
                print(f"  ✗ Karakter '{letter}' TIDAK ada di node")
                print(f"  → Membuat node baru untuk '{letter}'")
                current[letter] = {}
            else:
                print(f"  ✓ Karakter '{letter}' sudah ada di node")
            
            # Pindah ke node berikutnya
            print(f"  → Pindah ke node: {letter}")
            current = current[letter]
            print(f"Current node setelah: {current}")
            print(f"Struktur trie sekarang:\n{json.dumps(self.root, indent=2)}")
        
        # Tambahkan end symbol
        print(f"\n--- FINAL STEP: Menambahkan end symbol '*' ---")
        current[self.end_symbol] = True
        print(f"Menandai '{word}' sebagai kata yang lengkap")
        print(f"Struktur trie final:\n{json.dumps(self.root, indent=2)}")
    
    def add(self, word: str) -> None:
        """Method add standar tanpa visualisasi"""
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = True

    def exists(self, word: str) -> bool:
        current = self.root
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return self.end_symbol in current

    def __init__(self) -> None:
        self.root = {}
        self.end_symbol = "*"

    def __str__(self) -> str:
        return json.dumps(self.root, sort_keys=True, indent=4)


if __name__ == "__main__":
    trie = TrieVisualization()

    trie.add_with_steps("he")
    
    trie.add_with_steps("hello")
    
    trie.add_with_steps("help")
    
    trie.add_with_steps("hi")
    
    print(f"\n{'='*60}")
    print("STRUKTUR TRIE FINAL:")
    print(f"{'='*60}")
    print(trie)
