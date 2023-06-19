"""
Create a function called personal_numbers that receives, as its first argument,
a name, and then an indefinite number of values.
The function should return the following message:
"{name}, the sum of your numbers is {sum_numbers}"
"""

def personal_numbers(name, *args):
    sum_numbers = sum(args)
    return f"{name}, the sum of your numbers is {sum_numbers}"
