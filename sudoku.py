from z3 import *
from itertools import combinations
from typing import List


def exactly_one(literals: List[bool]) -> bool:
    """
    Determines if there is exactly one truthy value in an array of booleans.

    :param literals List[bool]: An array of boolean literals.
    :return: `true` if there is exactly one truthy value.
    :rtype: bool
    """

    return And(
        [Or(Not(a), Not(b)) for a, b in combinations(literals, 2)] + [Or(literals)]
    )


def print_solution(model: z3.Model, literals: List[bool]) -> str:
    lines = []
    for i in range(9):
        lines.append([])
        for j in range(9):
            digit = 0
            for x in range(9):
                if model.evaluate(literals[i][j][x]):
                    digit = x + 1
            lines[i].append(digit)

    for line in lines:
        print(" ".join([str(x) for x in line]))


def sudoku_solver(grid: List[List[bool]]) -> str:
    """
    Sudoku: 9x9 grid
    For each cell, 9 possible different digits
    Literals: 9x9x9 grid
    """

    literals = [[[] for j in range(9)] for i in range(9)]
    for i in range(9):
        for j in range(9):
            for digit in range(9):
                literals[i][j] += [Bool(f"x_{i}_{j}_{digit}")]

    # Solver instance
    s = Solver()

    # Add the first set of constaints
    # Only one possible digit/value per cell
    for i in range(9):
        for j in range(9):
            s.add(exactly_one(literals[i][j]))

    # Each digit only appears once in each row
    for i in range(9):
        for x in range(9):
            row = [literals[i][j][x] for j in range(9)]
            s.add(exactly_one(row))

    # Each digit only appears once in each column
    for j in range(9):
        for x in range(9):
            col = [literals[i][j][x] for i in range(9)]
            s.add(exactly_one(col))

    # Each digit only appears once in each 3x3 subgrid
    for i in range(3):
        for j in range(3):
            for k in range(9):
                grid_cells = [
                    literals[3 * i + x][3 * j + y] for y in range(3) for x in range(3)
                ]
                s.add(exactly_one(grid_cells))

    # 0 represnts that the cell in the grid has no digit/value
    # If a cell has a set digit, the corresponding literal must also be set to true.
    for i in range(9):
        for j in range(9):
            if grid[i][j]:
                s.add(literals[i][j][grid[i][j]])

    if s.check() == "sat":
        print_solution(s.model(), literals)
    else:
        print("unsat")
