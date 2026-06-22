# Words with Prefix
In a trie, "hello", "help" and "hi" would be represented as:
```
{
	"h": {
		"e": {
			"l": {
				"l": {
					"o": {
						"*": True
					}
				},
				"p": {
					"*": True
				}
			}
		},
		"i": {
			"*": True
		}
	}
}
```

## Assignment
Complete the `search_level` function. This recursive function collects all complete words starting from the current trie level. It takes the current dictionary level, the accumulated prefix string, and the list of words found.
1. Check for complete words:
    - If the current level contains an end marker, add the current prefix to the words collection.
2. Process [each character](https://docs.python.org/3/library/stdtypes.html#dict-views) in the current level in [sorted order (alphabetical)](https://docs.python.org/3/library/functions.html#sorted). For each character (except end markers):
    - Extend the prefix with the current character (e.g., current_prefix + character, rather than modifying the prefix in place).
    - Recursively search the child level with the extended prefix.
3. Return all words found.

Complete the `words_with_prefix` function. This finds all words in the trie that begin with a given prefix.
1. Create an empty list to store matching words.
2. Keep track of the current trie level, starting at the root.
3. Iterate through each character in the prefix:
    - If the character doesn't exist in the current level, return an empty list: no words start with this prefix.
    - If the character does exist, move to the child level corresponding to the current character.
4. By now, the current level should correspond to the last character in the prefix. Use the `search_level` function to find all words starting from this level and return them.