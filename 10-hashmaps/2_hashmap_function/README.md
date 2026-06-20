# Hashmap Function
Let's build a toy hash map in Python. In the real world, you would almost always use the built-in Python dictionary if you need a hash map. However, just using a dictionary doesn't teach us about what's going on under the hood!

## Assignment
As it turns out, the binary search tree was overkill for profile lookups on the LockedIn website. We don't need any of the fancy ordered traversals or range queries after all - and because LockedIn is such a business failure (our CEO's words, not mine) we can store every user in memory, no need to save them to the hard drive.

Let's build a hashmap! We'll use the strings (usernames) as keys, and map them to user objects.

Complete the HashMap's key_to_index method. It should:
1. Take a key (string) as input
2. Calculate the sum of the Unicode values of all the characters in the string using Python's ord function
3. Mod (%) the sum by the length of the hashmap (which is built on top of a list) to get an index which should be an int
4. Return the index