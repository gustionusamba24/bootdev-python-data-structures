"""
Bubble Sort membandingankan elemen-elemen yang berdekatan dan menukarnya jika
berada dalam urutan yang salah. Algoritma ini terus berulang
hingga seluruh daftar elemen di dalam list terurut dengan benar.

Here's the pseudocode:

1. Set swapping to True
2. Set end to the length of the input list
3. While swapping is True:
    1. Set swapping to False
    2. For i from the 2nd element to end:
        - If the (i-1)th element of the input list is greater than the ith element:
            - Swap the (i-1)th element and the ith element
            - Set swapping to True
    3. Decrement end by one
4. Return the sorted list 
"""
def bubble_sort(nums: list[int]) -> list[int]:
    swapping = True
    end = len(nums)

    while swapping:
        swapping = False

        # debug 
        print("Current state of the list:", nums)
        print("Current end index:", end)
        
        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True

        # debug
        print("List after this pass:", nums)
        print("=" * 50)

        end -= 1

    return nums


# Test case
if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    sorted_nums = bubble_sort(nums)
    print("Sorted array is:", sorted_nums)