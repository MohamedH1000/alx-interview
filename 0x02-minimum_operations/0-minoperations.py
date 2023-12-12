#!/usr/bin/python3
"""
    given n charachters and determine the minimum number of operations
"""


def minOperations(n):
    """
        a function the calculates the fewest number of operations
        needed
    """

    jetzt = 1
    beginning = 0
    counter = 0
    while jetzt < n:
        remainder = n - jetzt
        if (remainder % jetzt == 0):
            beginning = jetzt
            jetzt += beginning
            counter += 2
        else:
            jetzt += beginning
            counter += 1
    return counter
