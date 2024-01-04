#!/usr/bin/python3
"""
N-Queens puzzle
"""
import sys

def is_safe(board, row, col, N):
    """Check if it's safe to place a queen at (row, col) on the board."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def print_solution(board):
    """Print the solution."""
    solution = []
    for i in range(len(board)):
        solution.append([i, board[i]])
    print(solution)

def solve(board, row, N):
    """Recursively solve the N-Queens problem."""
    if row == N:
        print_solution(board)
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve(board, row + 1, N)

def nqueens(N):
    """Solve the N-Queens problem for a given N."""
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [0] * N
    solve(board, 0, N)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens(N)
