def tsp(cities: list[int], paths: list[list[int]], dist: int) -> bool:
    all_paths = permutations(cities)
    for path in all_paths:
        total_distance = 0
        for i in range(1, len(path)):
            total_distance += paths[path[i - 1]][path[i]]
        if total_distance < dist:
            return True
    return False

# don't touch below this line


def permutations(arr: list[int]) -> list[list[int]]:
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res: list[list[int]], arr: list[int], n: int) -> list[list[int]]:
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res