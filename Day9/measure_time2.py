import timeit

declaration_1 = """
for_test(10)
"""

setup_1 = """
def for_test(number):
    my_list = []
    for num in range(1, number + 1):
        my_list.append(num)
    return my_list
"""

declaration_2 = """
while_test(10)
"""

setup_2 = """
def while_test(number):
    my_list = []
    counter = 1
    while counter <= number:
        my_list.append(counter)
        counter += 1
    return my_list
"""

length_1 = timeit.timeit(declaration_1, setup_1, number=1000000)
length_2 = timeit.timeit(declaration_2, setup_2, number=1000000)

print(length_1)
print(length_2)

