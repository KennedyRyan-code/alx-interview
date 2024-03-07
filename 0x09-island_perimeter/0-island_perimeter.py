#!/usr/bin/python3
"""
a function that returns the perimeter of the island described in grid
"""

def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid:
            grid: is a list of list of integers
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                # Check adjacent cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
