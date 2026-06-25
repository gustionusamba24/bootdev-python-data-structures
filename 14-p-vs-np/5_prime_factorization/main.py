import math


def prime_factors(n: int) -> list[int]:
    factors = []

    while n % 2 == 0:
        n = n // 2
        factors.append(2)

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n = n // i
            factors.append(i)

    if n > 2:
        factors.append(int(n))

    return factors
