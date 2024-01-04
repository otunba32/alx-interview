#!/usr/bin/python3

"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """Generate Pascal's Triangle up to the specified row `n`.

    Args:
        n (int): Number of rows in Pascal's Triangle.

    Returns:
        list: List of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[i - 1]
        curr_row = [1]

        for j in range(1, i):
            curr_row.append(prev_row[j - 1] + prev_row[j])

        curr_row.append(1)
        triangle.append(curr_row)

    return triangle

