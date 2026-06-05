"""
ORDER N - O(n)
O(n) is very common - When the number of steps in an algorithm grows at the same rate as its input size, 
it's classified as O(n)

For example, our find min algorithm from earlier is O(n):
1. Set min to positive infinity.
2. For each number in the list, compare it to min. If it is smaller, set min to that number.
3. min is now set to the smallest number in the list.

The input to the find min algorithm is a list of size n. 
Because we loop over each item in the input once, we add one step to our algorithm for each item in our list.

As we use find min with larger and larger inputs, 
the length of time it takes to execute the function grows at a steady linear pace. 
We can reasonably estimate the time it will take to run, based on a previous measurement.
"""
def find_max(nums: list[float]) -> float:
    max = float("-inf")

    for num in nums:
        if num > max:
            max = num

    return max