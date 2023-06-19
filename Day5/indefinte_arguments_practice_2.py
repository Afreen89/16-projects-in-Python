"""
Create a function called absolute_sum, which takes any number of arguments,
and returns the sum of their absolute values
(that is, it takes the non-negative values and adds them together,
in other words, considers them all - negative and positive - as positive).
"""

def absolute_sum(*args):
    total = 0
    for arg in args:
        absolute = abs(arg)
        total += absolute
    return total