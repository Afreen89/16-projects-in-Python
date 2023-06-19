"""
Create a function called sum_squares that takes any number of numeric arguments,
and returns the sum of their values squared.
For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).
"""


def sum_squares(*args):
    total = 0
    for arg in args:
        sqr = arg ** 2
        total += sqr
    return total


print(sum_squares(1, 2, 3))