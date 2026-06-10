"""
The implementation details of polynomial time
1. The input n represents the index of the desired Fibonacci number.
2. If n is less than or equal to 1, return the n.
3. Initialize three variables, grandparent = 0, parent = 1, and a current
   to store the new fibonacci number at each step.
4. Write a loop that iterates n - 1 times. 
   (For example, if n is 5, the loop will run 4 times to calculate F(2), F(3), F(4), and F(5)).
5. Inside the loop:
   1. Set current = grandparent + parent (this calculates the next Fibonacci number).
   2. Adjust the ancestors values (parent and grandparent) to maintain the sequence
6. Once the loop completes, return current.
"""

def fib(n: int) -> int:
    if n <= 1:
        return n

    grandparent = 0
    parent = 1
    current = 0

    for _ in range(2, n + 1):
        current = grandparent + parent
        grandparent = parent
        parent = current

    return current
    