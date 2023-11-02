#!/usr/bin/python3
import sys

"""Module to solve the N-Queens problem."""


def solve_nqueens(n):
    """
    Solve the N-Queens problem for a given board size.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Returns:
        List[List[Tuple[int, int]]]: A list of solutions.
    """
    def can_place(board, row, col):
        """
        Check if it's safe to place a queen at a given position on the board.

        Args:
            board (List[int]): The current state of the chessboard.
            row (int): The row to check for placement.
            col (int): The column to check for placement.

        Returns:
            bool: True if it's safe to place a queen, False otherwise.
        """
        for i in range(col):
            if board[i] == row or \
                board[i] - i == row - col or \
                board[i] + i == row + col:
                return False
        return True

    def place_queens(board, col, n):
        """
        Recursively place queens on the chessboard.

        Args:
            board (List[int]): The current state of the chessboard.
            col (int): The current column to place a queen.
            n (int): The size of the chessboard.

        Returns:
            bool: True if queens are successfully placed for a solution.
        """
        if col == n:
            result.append(board[:])
            return True
        res = False
        for i in range(n):
            if can_place(board, i, col):
                board[col] = i
                res = place_queens(board, col + 1, n) or res
        return res

    result = []  # List to store the solutions
    board = [-1] * n
    place_queens(board, 0, n)
    return [[(i, board[i]) for i in range(n)] for board in result]


def main():
    """
    Function to parse command-line arguments and execute N-Queens solver.
    """
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
