#!/usr/python3
"""
Island Perimeter:
    returns the perimter of the island described in the grid
"""


def island_perimeter(grid):
    """ Island perimeter function """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[1])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter
