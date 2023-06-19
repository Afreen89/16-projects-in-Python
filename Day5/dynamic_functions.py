# def check_3_digits(number):
#     return number in range(100, 1000)
#
# sum = 565 +322
# result = check_3_digits(sum)
# print(result)

# def check_3_digits(list1):
#
#     three_digits_list = []
#     for n in list1:
#         if n in range(100, 1000):
#             three_digits_list.append(n)
#         else:
#             pass
#     return three_digits_list
#
# result = check_3_digits([55, 808, 650])
# print(result)

#
# def all_positives(list1):
#     for n in list1:
#         if n < 0:
#             return False
#     return True
#
# result = all_positives([2,3, -100])
# # print(type(n))
# print(result)
# # [-50, 30, 4, 7, -6]

# def sum_less(list1):
#     total = 0
#     numbers = []
#     for n in list1:
#         if n in range(0, 1000):
#             total += n
#             numbers.append(n)
#     return total, numbers
#
# print(sum_less([40, 30, 500, 765, 1200]))

numbers = [1, 2, 3, 4, 5, 6, 9.5]
def count_even(list1):
    even_values = [n for n in numbers if n % 2 == 0]
    return len(even_values)

print(count_even(numbers))






