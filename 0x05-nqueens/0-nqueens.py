#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    sabbora = []
    [sabbora.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in sabbora]
    return (sabbora)


def board_deepcopy(sabbora):
    """Return a deepcopy of a chessboard."""
    if isinstance(sabbora, list):
        return list(map(board_deepcopy, sabbora))
    return (sabbora)


def get_solution(sabbora):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(sabbora)):
        for c in range(len(sabbora)):
            if sabbora[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(sabbora, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no
    longer be played are X-ed out.
    """
    for c in range(col + 1, len(sabbora)):
        sabbora[row][c] = "x"
    for c in range(col - 1, -1, -1):
        sabbora[row][c] = "x"
    for r in range(row + 1, len(sabbora)):
        sabbora[r][col] = "x"
    for r in range(row - 1, -1, -1):
        sabbora[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(sabbora)):
        if c >= len(sabbora):
            break
        sabbora[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        sabbora[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(sabbora):
            break
        sabbora[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(sabbora)):
        if c < 0:
            break
        sabbora[r][c] = "x"
        c -= 1


def recursive_solve(sabbora, row, queens, solutions):
    """Recursively solve an N-queens puzzle.
    """
    if queens == len(sabbora):
        solutions.append(get_solution(sabbora))
        return (solutions)

    for c in range(len(sabbora)):
        if sabbora[row][c] == " ":
            tmp_board = board_deepcopy(sabbora)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    sabbora = init_board(int(sys.argv[1]))
    solutions = recursive_solve(sabbora, 0, 0, [])
    for a in solutions:
        print(a)
