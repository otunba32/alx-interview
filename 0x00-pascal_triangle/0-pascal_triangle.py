#!/usr/bin/python3

"""
Pascal's Triangle
"""

def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = []
        for x in range(i + 1):
            if x == 0 or x == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][x] + triangle[i - 1][x - 1])
        triangle.append(row)
    return triangle

"""# Call the function with n = 5
result = pascal_triangle(5)
print(result)"""

