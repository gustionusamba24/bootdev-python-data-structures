import math


def prime_factors(n: int) -> list[int]:
    factors = []
    print(f"Finding prime factors of {n}...")
    print(f"Current prime factors: {factors}")

    while n % 2 == 0:
        n = n // 2
        factors.append(2)
        print(f"Found prime factor: 2, Remaining number: {n}")

    # By now, the n is odd, so we can skip even numbers and check only odd numbers starting from 3
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            n = n // i
            factors.append(i)
            print(f"Found prime factor: {i}, Remaining number: {n}")

    if n > 2:
        factors.append(int(n))
        print(f"Found prime factor: {n}, Remaining number: 1")

    return factors

if __name__ == "__main__":
    test_numbers = [56, 57, 315, 512]

    for number in test_numbers:
        print(f"\nPrime factors of {number}: {prime_factors(number)}")
        print("=" * 60)   
