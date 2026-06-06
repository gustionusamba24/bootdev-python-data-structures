"""
Algoritma O(log(n)) hanya sedikit lebih lambat daripada O(1),
tetapi jauh lebih cepat daripada O(n).
Mereka tumbuh sesuai dengan ukuran input n, tetapi pertumbuhan mereka sesuai dengan logaritma dari input,
bukan dengan input itu sendiri.

Binary search merupakan contoh umum dari algoritma O(log(n)). 
Binary search bekerja dengan membagi daftar yang sudah diurutkan menjadi dua bagian dan menentukan apakah elemen yang dicari berada di bagian kiri atau kanan.
Dengan setiap langkah, algoritma ini mengurangi jumlah elemen yang harus diperiksa menjadi setengah, sehingga waktu eksekusinya tumbuh secara logaritmik terhadap ukuran input.
"""

"""
Pseudocode
Given two inputs:

    - A list of n elements sorted from least to greatest
    - A target value:
Do the following:

    - Set low = 0 and high = n - 1.
    - While low <= high:
        - Set median (the position of the middle element) to (low + high) // 2, which is the greatest integer less than or equal to (low + high) / 2
        - If list[median] == target, return True
        - Else if list[median] < target, set low to median + 1
        - Otherwise set high to median - 1
    - Return False
At each iteration of loop, we halve the list. Which makes the algorithm O(log(n)). In other words, to add one more step to the runtime, we'd have to double the size of the input. Binary searches are fast.

Assignment
We have a popular influencer using our LockedIn app, and she needs to be able to quickly search for posts from a particular day. This function will be the backbone of her search screen.
"""

def binary_search(target: int, arr: list[int]) -> bool:
    low = 0
    high = len(arr) - 1

    while low <= high:
        median = (low + high) // 2

        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median - 1

    return False