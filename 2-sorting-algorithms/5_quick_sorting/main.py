"""
QUICK SORT

Quick sort adalah metode sorting yang efisien dan banyak digunakan dalam production. 
Seperti halnya merge sort, quick sort menggunakan pendekatan divide and conquer.
Divide:
- Select a pivot element that will preferably end up close to the center of the sorted pack
- Move everything onto the "greater than" or "less than" side of the pivot
- The pivot is now in its final position
- Recursively repeat the operation on both sides of the pivot

Conquer:
- The array is sorted after all elements have been through the pivot operation
"""

"""
PSEUDOCODE
- Select a "pivot" element - We'll arbitrarily choose the last element in the list.
- Move through all the elements in the list and swap them around until all 
  the numbers less than the pivot are on the left, and the numbers greater 
  than the pivot are on the right.
- Move the pivot between the two sections where it belongs.
- Recursively repeat for both sections.
"""

"""
ASSIGNMENT
We now have two sorting algorithms on our LockedIn backend! 
It is a bit annoying to maintain both in the codebase. 
Quicksort is fast on large datasets just like merge sort, 
but is also lighter on memory usage. Let's use quick sort 
for both follower count and influencer revenue sorting!

Complete the quick_sort and partition functions according to the given algorithms.

The process is started with quick_sort(A, 0, len(A)-1).
"""

"""
INSTRUCTIONS for quick_sort:
1. Complete quick_sort(nums, low, high)
    1. If low is less than high:
        1. Partition the input list using the partition function and store the returned "middle" index
        2. Recursively call quick_sort on the elements left of the pivot (low to middle - 1)
        3. Recursively call quick_sort on the elements right of the pivot (middle + 1 to high)
"""
def quick_sort(nums: list[int], low: int, high: int) -> None:
    if low < high:
        middle = partition(nums, low, high)
        quick_sort(nums, low, middle - 1)
        quick_sort(nums, middle + 1, high)


"""
INSTRUCTIONS for partition:
2. partition(nums, low, high):
    1. Set pivot to the element at index high
    2. Set i to the index before low
    3. For each index (j) in range(low, high):
        1. If the element at index j is less than the pivot:
            1. Increment i by 1
            2. Swap the element at index i with the element at index j
    4. Swap the element at index i + 1 with the element at index high (the pivot's position)
    5. Return i + 1 (the pivot's new index)
"""
def partition(nums: list[int], low: int, high: int) -> int:
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1