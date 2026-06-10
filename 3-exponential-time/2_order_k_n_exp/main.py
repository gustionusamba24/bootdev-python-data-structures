"""
ORDER K^N EXPONENTIAL

ASSIGNMENT:
Completet the letter combinations function using the algorithm outlined below. 
It takes string of digits and returns a list of strings of letters.
1. If the input string is empty, return an empty list.
2. Define a result list to hold the output strings. 
   Have it contain just an empty string to start (we need that one element to build on).
3. Iterate over the input digits. For each of them:
    1. If the digit is any invalid character, i.e. not found 
       in the provided digit_to_letters dictionary, raise a ValueError to abort the function:
       raise ValueError(f"invalid digit: {digit}")
    2. Get the string of letters that can be represented by the current digit, from digit_to_letters.
    3. Define a new_result list - empty to start with.
    4. Enter two nested for loops:
        1. For each existing letter combo in result, iterate over each letter in the current digit's letters.
        2. Append combo + letter to new_result.
    5. After the two nested loops, but still inside the main loop over digits, set result equal to new_result.
4. After the main loop, return the result.
"""

def letter_combinations(digits: str) -> list[str]:
    print("=" * 160)
    
    if len(digits) == 0:
        return []

    result: list[str] = [""]

    for digit in digits:
        if digit not in digit_to_letters:
            raise ValueError(f"invalid digit: {digit}")

        letters = digit_to_letters[digit]
        new_result: list[str] = []

        # debug
        print(f"digit: {digit}, letters: {letters}")
        for combo in result:
            for letter in letters:
                new_result.append(combo + letter)
                print(f"combo: {combo}, letter: {letter}, new_result: {new_result}")

        result = new_result
        print(f"result after processing digit {digit}: {result}")
        print("-" * 80)

    print("final result =")
    return result


# Don't touch below this line

digit_to_letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

if __name__ == "__main__":
    print(letter_combinations(""))
    print(letter_combinations("67"))
    # print(letter_combinations("43556"))
    # print(letter_combinations("2668338"))