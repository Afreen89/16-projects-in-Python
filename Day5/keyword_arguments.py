def a_sum(**kwargs):

    total = 0

    for key, value in kwargs.items():
        print(f"{key} = {value}")

        total += value

    return total
#
# args = [100, 200, 400]


# def tess(number1, number2, *args, **kwargs):
#     print(f"The first number is {number1}")
#     print(f"The second number is {number2}")
#
#     for arg in args:
#         print(f"arg = {arg}")
#
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")
#
# kwargs = {'x':'one', 'y':'two', 'z':'three'}
# tess(15, 50, *args, **kwargs)
# # print(a_sum(x=3, y=5, z=2))
#

