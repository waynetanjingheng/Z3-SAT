from z3 import *
from itertools import combinations


def exactly_one(literals):
    """
    Determines if there is exactly one truthy value in an array of booleans.

    :param literals List[bool]: An array of boolean literals.
    :return: `true` if there is exactly one truthy value.
    :rtype: bool
    """

    return And([Or(Not(a), Not(b)) for a, b in combinations(literals, 2)] + [Or(literals)])
