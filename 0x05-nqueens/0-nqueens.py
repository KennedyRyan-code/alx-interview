#!/usr/bin/python3
"""
N queens puzzle is the challenge of placing N non-attacking
queens on an N×N chessboard
"""
import sys


class NQueen:
    """ Class for solving N Queen Problem """

    def __init__(self, n):
        self.n = n
        self.solutions = []

    def is_safe(self, board, row, col):
        """ Check the left side of the current row """

        for i in range(col):
            if board[row][i] == 1:
                return False

        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, self.n), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def solve_nqueens_util(self, board, col):
        """If all queens are placed, append the solution"""

        if col == self.n:
            self.solutions.append([[row, col] for row in range(self.n) if board[row][col - 1] == 1])
            return True

        res = False
        for i in range(self.n):
            if self.is_safe(board, i, col):
                board[i][col] = 1
                res = self.solve_nqueens_util(board, col + 1) or res
                board[i][col] = 0  # backtrack if the solution isn't valid
        return res

    def solve_nqueens(self):
        board = [[0] * self.n for _ in range(self.n)]
        if not self.solve_nqueens_util(board, 0):
            print("No solution exists")
            return

        for solution in self.solutions:
            print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        nqueen = NQueen(N)
        nqueen.solve_nqueens()
    except ValueError:
        print("N must be a number")
        sys.exit(1)
