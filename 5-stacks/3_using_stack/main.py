"""
LockedIn supports a basic scripting language. 
It allows technically savvy HR managers to write scripts 
that can automate repetitive tasks on the platform. 
The language makes use of parentheses to group operations together, 
and we need to be able to check if the parentheses in a script are balanced.
"""

"""
BALANCED PARENTHESES    
Parentheses are balanced when each parenthesis has a 
corresponding parenthesis, and the pairs of parentheses are properly nested. For example:
- ()
- ()()
- ((()))
- (()(()))

UNBALANCED PARENTHESES
- (
- ())
- (()()
- (()))
- )(
"""

"""
ASSIGNMENT
Complete the is_balanced function

It takes a string as input and returns True 
if the parentheses in the string are balanced, and False otherwise. 
Use an instance of the provided Stack class in stack.py to keep track of the parentheses.
"""

from stack import Stack


def is_balanced(input_str: str) -> bool:
    stack = Stack()

    for char in input_str:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.size() == 0:
                return False
            stack.pop()
    return stack.peek() is None
