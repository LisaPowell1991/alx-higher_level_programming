#!/usr/bin/python3

"""
N-Queens Solver

This module provides a program to solve the N-Queens problem
and print all possible solutions.

Usage: nqueens N
If the user called the program with the wrong number of arguments,
print Usage: nqueens N, followed by a new line, and exit with the status 1.
where N must be an integer greater or equal to 4.
If N is not an integer, print N must be a number,
followed by a new line, and exit with the status 1.
If N is smaller than 4, print N must be at least 4,
followed by a new line, and exit with the status 1.
The program should print every possible solution to the problem.
One solution per line.
Format: see example.
You don’t have to print the solutions in a specific order.
You are only allowed to import the sys module.
"""


import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[rw][col]

    Args:
    board (list): The chessboard represented as a 2D list
    row (int): The current row being checked
    col (int): The current col being checked

    Returns:
    bool: True if it's safe to place a queen at a specific position,
    false orherwise.
    """

    n = len(board)

    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    else:
        return True


def solve_nqueens(n):
    """
    Solve the N-Queens problem and print all possible solutions.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Raises:
        ValueError: If n is less than 4.

    Returns:
        None
    """

    if n < 4:
        raise ValueError("N must be at least 4")

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(row):
        """
        Recursively explore all possible queen placements on the board.

        Args:
            row (int): The current row being considered for queen placement.

        Returns:
            None
        """

        if row == n:
            solutions.append([
                [i, j]
                for i in range(n)
                for j in range(n)
                if board[i][j] == 1
                ])
        else:
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 1
                    backtrack(row + 1)
                    board[row][col] = 0

    backtrack(0)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)
