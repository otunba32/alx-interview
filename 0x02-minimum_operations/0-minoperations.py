#!/usr/bin/python3
"""
If the number of is divisible by n, copy and paste
else paste only
"""

def minOperations(n):
    """
    Returns the number of operations
    required to reach a certain n
    """
    len_H =  1  # original length of H 
    len_copied_H = 0 # no copies are made at first
    total_operations = 0 # no operation has been made

    # break the loop when len_h == n
    while len_H < n:
        if n % len_H == 0:
            # performs copy and paste (2 operation)
            total_operations += 2
            len_copied_H = len_H
            len_H *= 2

        else:
            # perform only 1 operation that is paste only
            total_operations += 1
            len_H += len_copied_H
    return total_operations