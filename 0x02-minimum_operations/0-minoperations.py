#!/usr/bin/python3
'''
The minimum operations algorithim.
'''


def minOperations(n):
    '''
    Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if n <= 1:
        return 0

    operations = 0
    clipboard = 1
    buffer = 1

    while buffer < n:
        if n % buffer == 0:
            clipboard = buffer
            operations += 2
        buffer += clipboard

    return operations if buffer == n else 0
