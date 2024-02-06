#!/usr/bin/python3

""" an island perimeter to be find by this function """


def island_perimeter(grd):
    """
    Input: List of Lists
    Perimeter of the island to be returned
    """
    number = 0
    row = len(grd)
    col = len(grd[0]) if row else 0

    for a in range(len(grd)):
        for b in range(len(grd[a])):

            idx = [(a - 1, b), (a, b - 1), (a, b + 1), (a + 1, b)]
            check = [1 if c[0] in range(row) and c[1] in range(col) else 0
                     for c in idx]

            if grd[a][b]:
                number += sum([1 if not r or not grd[c[0]][c[1]] else 0
                              for r, c in zip(check, idx)])

    return (number)
