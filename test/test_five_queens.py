from five_queens import at_most_one
from z3 import Bool, Solver, sat, unsat


def test_at_most_one_sat():
    """
    Tests the `at_most_one` function from the five queens problem solver.

    :param literals List[bool]: An array of boolean literals.
    :return: `true` if there is at most one truthy value.
    :rtype: bool
    :expected test result: sat
    """

    test_solver = Solver()

    x = [[Bool(f"x_{i}_{j}") for j in range(5)] for i in range(5)]

    for i in range(5):
        t = [x[c][i] for c in range(5)]
        test_solver.add(at_most_one(t))
        test_solver.add(at_most_one(x[i]))

    assert test_solver.check() == sat


def test_at_most_one_unsat():
    """
    Tests the `at_most_one` function from the five queens problem solver.

    :param literals List[bool]: An array of boolean literals.
    :return: `true` if there is at most one truthy value.
    :rtype: bool
    :expected test result: unsat
    """

    test_solver = Solver()

    literals_more_than_one_true = [True, True, False]

    test_solver.add(at_most_one(literals_more_than_one_true))

    assert test_solver.check() == unsat
