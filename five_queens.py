from z3 import Bool, And, Or, Not, Solver
from itertools import combinations
from typing import List


def at_most_one(literals: List[bool]) -> bool:
    """
    Determines if there is at most one truthy value in an array of booleans.

    :param literals List[bool]: An array of boolean literals.
    :return: `true` if there is at most one truthy value.
    :rtype: bool
    """

    return And([Or(Not(a), Not(b)) for a, b in combinations(literals, 2)])


# Create all the literals on the board
board = [[Bool(f"x_{i}_{j}") for j in range(5)] for i in range(5)]

# Create the solver instance
s = Solver()

# Add all the constraints
# Ensure at least 5 queens on the board
for row in range(5):
    s.add(
        Or(board[row])
    )  # at least one queen per row, checking the disjunction of each row

# Constraints: at most one queen per row
# and at most one queen per column
for i in range(5):
    col = [board[c][i] for c in range(5)]
    s.add(at_most_one(col))
    s.add(at_most_one(board[i]))

# Constraints: at most one queen per diagonal
for i in range(4):
    diag_1 = [board[i + j][j] for j in range(5 - i)]
    diag_2 = [board[i + j][4 - j] for j in range(5 - i)]
    diag_3 = [board[4 - (i + j)][j] for j in range(5 - i)]
    diag_4 = [board[4 - (i + j)][4 - j] for j in range(5 - i)]

    s.add(at_most_one(diag_1))
    s.add(at_most_one(diag_2))
    s.add(at_most_one(diag_3))
    s.add(at_most_one(diag_4))

print(s.check())
