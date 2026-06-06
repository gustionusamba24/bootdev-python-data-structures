"""
Order 1 atau O(1) berarti tidak peduli seberapa besar inputnya, waktu eksekusi algoritma akan selalu konstan.

Di python, dictionary menawarkan kemampuan untuk mencari item berdasarkan key,
yang merupakan operasi yang tidak bergantung pada ukuran dictionary tersebut. 

Pencarian menggunakan dictionary memiliki kompleksitas O(1). 
"""

"""
We need to be able to search our LockedIn user base more quickly! 
Our users are complaining that the search bar is painfully slow. 
You'll notice that if you run the code in its current state, it will take a very long time.
The find_last_name function takes:
- names_dict: a dictionary of first_name -> last_name.
- first_name: a string.

If first_name is a key in the dictionary, find_last_name returns the associated last name. If the key is not found, it returns None.
"""
def find_last_name(names_dict: dict[str, str], first_name: str) -> str | None:
    try:
        return names_dict[first_name]
    except KeyError:
        return None