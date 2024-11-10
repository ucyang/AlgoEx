N = int(input())
BOARD = [list(input()) for _ in range(N)]


def get_max_score():
    max_seq = 0

    for i in range(N):
        row_seq = 0
        col_seq = 0

        for j in range(1, N):
            if BOARD[i][j - 1] == BOARD[i][j]:
                row_seq += 1
            else:
                if row_seq + 1 > max_seq:
                    max_seq = row_seq + 1
                row_seq = 0

            if BOARD[j - 1][i] == BOARD[j][i]:
                col_seq += 1
            else:
                if col_seq + 1 > max_seq:
                    max_seq = col_seq + 1
                col_seq = 0

        max_seq = max(max_seq, row_seq + 1, col_seq + 1)

    return max_seq


max_seq = 0

for i in range(N):
    for j in range(N):
        if j < N - 1 and BOARD[i][j] != BOARD[i][j + 1]:
            BOARD[i][j], BOARD[i][j + 1] = BOARD[i][j + 1], BOARD[i][j]
            max_seq = max(max_seq, get_max_score())
            BOARD[i][j], BOARD[i][j + 1] = BOARD[i][j + 1], BOARD[i][j]
        if i < N - 1 and BOARD[i][j] != BOARD[i + 1][j]:
            BOARD[i][j], BOARD[i + 1][j] = BOARD[i + 1][j], BOARD[i][j]
            max_seq = max(max_seq, get_max_score())
            BOARD[i][j], BOARD[i + 1][j] = BOARD[i + 1][j], BOARD[i][j]

print(max_seq)
