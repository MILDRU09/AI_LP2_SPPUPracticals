def safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_bt(board, row, n):
    if row == n:
        print(board)
        return

    for col in range(n):
        if safe(board, row, col):
            board[row] = col
            solve_bt(board, row + 1, n)
            board[row] = -1


# Run
n = 4
board = [-1] * n
print("Backtracking:")
solve_bt(board, 0, n)