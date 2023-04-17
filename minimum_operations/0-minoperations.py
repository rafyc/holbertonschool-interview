#!/usr/bin/python3
"""
method that calculates the fewest number of operations needed to result
"""


def minOperations(n):
    if n == 1 or n == 0:
        return 0

    ops = 0
    curr = 1
    copy = 0

    while curr < n:
        if n % curr == 0:
            copy = curr
        if copy > 0:
            ops += 2  # copy-all and paste
            curr += copy
            copy = 0
        else:
            ops += 1  # paste
            curr += curr

        if curr > n:
            return 0

    return ops
