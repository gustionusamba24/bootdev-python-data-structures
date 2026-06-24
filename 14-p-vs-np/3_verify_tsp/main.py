def verify_tsp(paths: list[list[int]], dist: int, actual_path: list[int]) -> bool:
    total_distance = 0
    for i in range(1, len(actual_path)):
        total_distance += paths[actual_path[i - 1]][actual_path[i]]
    return total_distance < dist
