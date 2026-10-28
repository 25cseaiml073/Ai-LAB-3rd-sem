def print_board(board):
    for row in board:
        print(" ".join(row))

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1
    while i >= 0 and j < 8:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve(board, row):
    if row == 8:
        return True

    for col in range(8):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            if solve(board, row + 1):
                return True
            board[row][col] = '.'

    return False

if __name__ == '__main__':
    board = [['.' for _ in range(8)] for _ in range(8)]
    if solve(board, 0):
        print("Solution for 8-Queen problem:")
        print_board(board)
    else:
        print("No solution exists")

""" OUTPUT:
Solution for 8-Queen problem:
Q . . . . . . .
. . . . Q . . .
. . . . . . . Q
. . . . . Q . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .
"""
