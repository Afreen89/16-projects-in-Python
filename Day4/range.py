# for num in range(20, 31, 2):
#     print(num)

#####################################
#
# print(my_list)
# my_list = list(range(1, 101))

my_list = list(range(1, 16))
sum_squares = 0
for num in my_list:
    square = num ** 2
    sum_squares = sum_squares + square
print(sum_squares)