def exponential_growth(n: int, factor: int, days: int) -> list[int]:
    growth_sequence: list[int] = [n]

    for _ in range(days):
        growth_sequence.append(growth_sequence[-1] * factor)
    return growth_sequence