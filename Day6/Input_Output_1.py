my_file = open('test.txt')

one_line = my_file.read()
print(one_line)
#
# one_line = my_file.readline()
# print(one_line.rstrip())

# for l in my_file:
#     print("Here it says: " + l)

my_file.close()