# Longest Common Prefix
Let's use our Trie to find the longest common prefix of a list of words. This feature can be used in LockedIn to display suggestions when users are searching for their connections.

## Assignment
Complete the `longest_common_prefix` method. It returns the longest common prefix among the words in the trie.
1. Initialize a variable current that references the root of the trie
2. Initialize a variable prefix to an empty string
3. Enter a forever while loop:
    1. Create an empty children list.
    2. Iterate over the keys of current. Append each key that isn't the end_symbol to children.
    3. If the end_symbol is in current, or there isn't exactly one child, break the loop.
    4. Otherwise, append the single child character to the prefix string and update current to point to that child's dictionary.
4. Return the prefix string.

## Tips
1. You can access just the keys of a dictionary with the .keys() method.
2. Here's the syntax for an intentional infinite loop. Always remember to include an exit condition so it doesn't actually continue forever.