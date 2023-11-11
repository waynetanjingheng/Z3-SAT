from z3 import *
from sudoku import exactly_one


def test_exactly_one_sat():
    """
    Tests the `exactly_one` function from the five queens problem solver.

    :param literals List[bool]: An array of boolean literals.
    :return: `true` if there is exactly one truthy value.
    :rtype: bool
    :expected test result: sat
    """

    test_solver = Solver()

    literals_one_true = [True, False, False]

    test_solver.add(Or(exactly_one(literals_one_true)))

    assert test_solver.check() == sat


def test_exactly_one_unsat():
    """
    Tests the `exactly_one` function from the five queens problem solver.

    :param literals List[bool]: An array of boolean literals.
    :return: `true` if there is exactly one truthy value.
    :rtype: bool
    :expected test result: unsat
    """

    test_solver = Solver()

    literals_none_true = [False, False, False]
    literals_more_than_one_true = [True, True, False]

    test_solver.add(
        Or(exactly_one(literals_none_true), exactly_one(literals_more_than_one_true))
    )

    assert test_solver.check() == unsat
