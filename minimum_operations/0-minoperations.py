#!/usr/bin/python3
"""
method that calculates the fewest number of operations needed to result
"""


def minOperations(n):
    if n == 1 or n == 0:
        return 0

    ops = 0
    factor = 2

    while n > 1:
        if n % factor == 0:
            n //= factor
            ops += factor
        else:
            factor += 1

    return ops
