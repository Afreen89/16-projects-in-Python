# file = open('test1.txt', 'w')
# my_list = ["Hello", "world", "here", "I am"]
#
# for w in my_list:
#     file.writelines(w + '\n')
#
# file.close()


file = open('test.txt', 'a')
file.write('welcome')

file.close()

one_line = my_file.read()
print(one_line)