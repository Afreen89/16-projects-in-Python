"""
Create a function called reduce_list() that takes a list (numbers) as an argument, and returns also a list,
but removing duplicates (leaving only one of the numbers if there are duplicates) and removing the highest value.
The order of the elements can be changed. For example, if given the list [1,2,15,7,2] it should return [1,2,7].
Create a function called average() that can receive as an argument the list returned by the previous function,
and that calculates the average of its values. It should return the result (a float), without printing it.
"""

numerical = [1, 2, 15, 7, 2]

def reduce_list(numbers):
    numbers.remove(max(numbers))
    my_list = sorted(list(dict.fromkeys(numbers)))
    return my_list

def average(list1):
    my_sum = sum(list1) / len(list1)
    return my_sum

blue = reduce_list(numerical)
average(blue)



