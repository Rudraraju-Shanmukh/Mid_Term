def calculate_std_deviation_rec(numbers):
    n = len(numbers)
    if n < 2:
        return 0.0

    mean = sum(numbers) / n
    squared_diffs = [(x - mean) ** 2 for x in numbers]
    variance = calculate_variance(squared_diffs, n)
    std_deviation = variance ** 0.5

    return std_deviation


def calculate_variance(squared_diffs, n):
    if n == 1:
        return squared_diffs[0]
    else:
        return ((n - 1) / n) * calculate_variance(squared_diffs[:-1], n - 1) + (squared_diffs[-1] / n)


def calculate_std_deviation_itr(numbers):
    n = len(numbers)
    if n < 2:
        return 0.0

    mean = sum(numbers) / n
    squared_diffs = [(x - mean) ** 2 for x in numbers]
    variance = sum(squared_diffs) / n
    std_deviation = variance ** 0.5

    return std_deviation


numbers = [1, 2, 3, 4, 5]

std_deviation_iter = calculate_std_deviation_itr(numbers)
print(f"standard deviation using iteration method is {std_deviation_iter}")
std_deviation_recur = calculate_std_deviation_rec(numbers)
print(f"standard deviation using recursion method is {std_deviation_recur}")
