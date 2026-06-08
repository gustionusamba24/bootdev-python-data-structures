"""
Merge Sort merupakan recursive sorting algorithm dan
cenderung lebih cepat daripada bubble sort.
- divide: membagi masalah besar menjadi masalah yang lebih kecil dan secara rekursif
    menyelesaikan masalah yang lebih kecil tersebut.
- conquer: menggabungkan solusi dari masalah yang lebih kecil untuk menyelesaikan masalah besar.
"""

"""
The algorithm consists of two separate functions, merge_sort() and merge().

* merge_sort() : 
merge_sort() divides the input array into two halves, 
calls itself on each half, and 
then merges the two sorted halves back together in order.

* merge() :
The merge() function merges two already sorted lists back into a single sorted list. 
At the lowest level of recursion, the two "sorted" lists will each only have one element. 
Those single element lists will be merged into a sorted list of length two, 
and we can build from there.
"""


"""
A. merge_sort() pseudocode
Input: A, an unsorted list of integers

1. If the length of A is less than 2, it's already sorted so return it
2. Split the input array into two halves down the middle
3. Call merge_sort() twice, once on each half
4. Return the result of calling merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls
"""
def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums

    mid = len(nums) // 2
    left_half = merge_sort(nums[:mid])
    right_half = merge_sort(nums[mid:])
    return merge(left_half, right_half)


"""
B. merge() pseudocode
Inputs: A and B. Two sorted lists of integers

1. Create a new final list of integers.
2. Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
3. Use a loop to compare the current elements of A and B:
- While i < len(A) and j < len(B), compare A[i] and B[j].
- Append the smaller or equal value to final.
- Increment the index for the list you just took from.
- Stop when either list is exhausted.
4. After comparing all the items, there may be some items left over in either A or B. Add those extra items to the final list.
5. Return the final list.
"""
def merge(first: list[int], second: list[int]) -> list[int]:
    final: list[int] = []
    i = j = 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1

    # Append any remaining elements from either list
    final.extend(first[i:])
    final.extend(second[j:])

    return final