"""
INSERTION SORTING
Algoritma pengurutan sederhana yang cara kerjanya mirip dengan bagaimana kita mengurutkan kartu di tangan.
Algoritma ini membagi array menjadi 2 bagian, yaitu bagian yang sudah terurut di sebelah kiri dan
bagian yang belum terurut di sebelah kerja. 
Elemen dari bagian yang belum terurut akan diambil satu per satu, 
lalu dimasukkan (disisipkan) ke posisi yang tepat pada bagian yang sudah terurut.

Perbandingan Insertion sort dan Merge sort:
- Insertion sort menggunakan konsep penyisipan dan incremental, sedangkan merge sort menggunakan divide and conquer.
- Insertion sort lebih efisien untuk dataset kecil atau hampir terurut, 
  sedangkan merge sort lebih efisien untuk dataset besar dan tidak terurut.
- Insertion sort memiliki kompleksitas waktu O(n^2) dalam kasus terburuk, 
  sedangkan merge sort memiliki kompleksitas waktu O(n log n) dalam semua kasus.
- Sangat cepat dan efisien karena overhead algoritma yang rendah, 
  sedangkan merge sort memiliki overhead yang lebih tinggi karena penggunaan rekursi dan penyimpanan tambahan untuk penggabungan.
"""

"""
INSTRUCTIONS
Our influencers want to sort their affiliate deals by revenue. 
None of our users have more than a couple hundred affiliate deals, 
so we don't need an n * log(n) algorithm like merge sort. 
In fact, insertion_sort can be faster than merge_sort, and uses less of our server's memory.
Complete the insertion_sort function according to the given pseudocode:

1. For each index in the input list, starting with the second element:
    1. Set a j variable to the current index
    2. While j is greater than 0 and the element at index j-1 is greater than the element at index j:
        - Swap the elements at indices j and j-1
        - Decrement j by 1
2. Return the list
"""


def insertion_sort(nums: list[int]) -> list[int]:
  for i in range(1, len(nums)):
    j = i
    print(f"i: {i}, j: {j}, nums: {nums}")
    while j > 0 and nums[j - 1] > nums[j]:
      nums[j], nums[j - 1] = nums[j - 1], nums[j]
      j -= 1
  return nums

if __name__ == "__main__":
  print(insertion_sort([5, 2, 4, 6, 1, 3])) # [1, 2, 3, 4, 5, 6]
  print(insertion_sort([31, 41, 59, 26, 41, 58])) # [26, 31, 41, 41, 58, 59]