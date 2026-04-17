def solve_bb(n):
    def solve(row):
        if row == n:
            print(board)
            return

        for col in range(n):
            if not col_used[col] and not d1[row+col] and not d2[row-col+n-1]:
                board[row] = col
                col_used[col] = d1[row+col] = d2[row-col+n-1] = True

                solve(row + 1)

                col_used[col] = d1[row+col] = d2[row-col+n-1] = False
                board[row] = -1

    board = [-1]*n
    col_used = [False]*n
    d1 = [False]*(2*n)
    d2 = [False]*(2*n)

    print("Branch & Bound:")
    solve(0)


# Run
solve_bb(4)