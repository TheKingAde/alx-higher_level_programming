#!/usr/bin/python3
import sys


def solve_nqueens(n):
    def can_place(board, row, col):
        for i in range(col):
            if board[i] == row or \
                board[i] - i == row - col or \
                board[i] + i == row + col:
                return False
        return True

    def place_queens(board, col, n):
        if col == n:
            result.append(board)
            return True
        res = False
        for i in range(n):
            if can_place(board, i, col):
                board[col] = i
                res = place_queens(board, col + 1, n) or res
        return res

    result = []
    board = [-1] * n
    place_queens(board, 0, n)
    return [[(i, board[i]) for i in range(n)] for board in result]

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    for solution in solve_nqueens(n):
        print(solution)

if __name__ == "__main__":
    main()
