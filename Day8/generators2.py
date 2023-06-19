# def my_generator():
#
#     x = 1
#     yield x
#
#     x += 1
#     yield x
#
#     x += 1
#     yield x
#
# g = my_generator()
#
# print(next(g))
# print(next(g))
# print(next(g))

def generator():
    num = 1
    while True:
        multi = num * 7
        num += 1
        yield multi


practice_generator = generator()

print(next(practice_generator))
print(next(practice_generator))
print(next(practice_generator))