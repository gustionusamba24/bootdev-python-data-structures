def get_num_guesses(length: int) -> int:
    num_of_possibilies = 0

    for i in range(length):
        num_of_possibilies += 26 ** (i + 1)
    return num_of_possibilies