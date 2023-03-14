def sum_white_primes_minus_black_primes(board):
    white_sum = 0
    black_sum = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if (i + j) % 2 == 0:  # white square
                if is_prime(board[i][j]):
                    white_sum += board[i][j]
            else:  # black square
                if is_prime(board[i][j]):
                    black_sum += board[i][j]

    return white_sum - black_sum


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = sum_white_primes_minus_black_primes(board)
print(f"sum of white primes minus the black primes in the board is {result}")
print(f"sum of white primes minus the black primes in the board is {result}")
