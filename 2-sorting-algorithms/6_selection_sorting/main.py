"""
SELECTION SORTING
Mempunyai konsep yang hampir sama dengan Bubble Sorting, tetapi
ini agak sedikit berbeda dibanding bubble sort. 
Jika bubble sort melakukan perbandingan pada elemen yang berdekatan secara terus-menerus,
di selection sort, dia mencari elemen terkecil dari seluruh array dan menukarnya dengan elemen di posisi paling depan.
"""

"""
INSTRUCTIONS
1. For each index
    1. Set smallest_idx to the current index (of the outer loop)
    2. For each index from i + 1 to the end of the list:
        1. If the number at the inner loop index is smaller than the number at smallest_idx, set smallest_idx to the inner loop index
    3. Swap the number at the outer loop index with the number at smallest_idx
2. Return the sorted list
"""


def selection_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        smallest_idx = i
        # debug
        print(f"i: {i}, smallest_idx: {smallest_idx}, value: {nums[smallest_idx]}, nums: {nums}")
        for j in range(i + 1, len(nums)):
            # debug
            print(f"j: {j}, value: {nums[j]}")
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
                # debug
                print(f"Updated smallest_idx: {smallest_idx}, value: {nums[smallest_idx]}")
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
        # debug
        print(f"After swap - i: {i}, nums: {nums}")
        print("-" * 40)
    return nums


if __name__ == "__main__":
    print(selection_sort([5, 3, 6, 2, 10]))