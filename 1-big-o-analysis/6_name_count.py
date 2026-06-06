def count_names(list_of_lists: list[list[str]], target_name: str) -> int:
    count = 0

    for list in list_of_lists:
        for item in list:
            if target_name == item:
                count += 1

    return count
