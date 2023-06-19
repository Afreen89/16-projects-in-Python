# my_list = ['a', 'b', 'c']
# index = 0

# for item in my_list:
#     print(index, item)
#     index += 1

# for index, item in enumerate(my_list):
#     print(index, item)
#
# for index, item in enumerate(range(50, 55)):
#     print(index, item)
#
# my_tuples = list(enumerate(my_list))
# print(my_tuples)

list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]
print(type(list_names))
for index, name in enumerate(list_names):
    if name.startswith("M"):
        print(index)
