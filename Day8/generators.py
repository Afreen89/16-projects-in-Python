"""
The basic function where we have to make a list to store some numbers
"""
def my_function():
    my_list = []
    for x in range(1, 5):
        my_list.append(x * 10)
    return my_list

"""
This is the generator function, no need to store memory, generate 
values of the list on spot
"""
def my_generator():
    for x in range(1, 5):
        yield x * 10


print(my_function())
print(my_generator())

g = my_generator()

print(next(g))
print(next(g))