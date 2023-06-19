"""
Create a function called return_distinct() that receives 3
integers as parameters.
If the sum of the 3 numbers is greater than 15, it must return
the highest number.
If the sum of the 3 numbers is less than 10, it must return the
lowest number.
If the sum of the 3 numbers is a value between 10 and 15
(included), then it must return the number with the
intermediate value.
"""


def return_distinct(num1, num2, num3):
    addition = num1 + num2 + num3
    numbers = [num1, num2, num3]
    if addition > 15:
        return max(numbers)
    elif addition < 10:
        return min(numbers)
    else:
        return (sorted(numbers))[1]


print(return_distinct(8, 4, 2))

"""
Write a function (you can name it whatever you want) that
takes any word as a parameter, and returns all of its unique
letters (without repetition) in alphabetical order.
For example, if when calling this function we pass the word
"entertaining", it should return ['a','e','g','i','n','r','t']
"""


def check_repetition(word):
    my_set = set()

    for letter in word:
        my_set.add(letter)

    my_list = list(my_set)
    my_list.sort()

    return my_list

    # return sorted((set(str(word))))


print(check_repetition("entertaining"))

"""
Write a function that requires an indefinite number of
arguments. What this function must do is return True if at any
time the number zero has been entered twice consecutively.
"""

def consecutive(*args):

    counter = 0

    for n in args:

        if counter + 1 == len(args):
            return False

        elif args[counter] == 0 and args[counter + 1] == 0:
            return True
        else:
            counter += 1

    return False


print(consecutive(8, 6, 0, 0, 3, 1, 2, 3, 5, 9))


"""
Write a function called count_primes() that requires a single
numeric argument.
This function must display on the screen how many prime
numbers there are in the range from zero to that number
included, and then return the number of prime numbers found.
Note: By convention 0 and 1 are not considered primes
"""


def count_prime_numbers(number):

    prime_numbers = [2]
    iteration = 3

    if number < 2:
        return 0

    while iteration <= number:
        for n in range(3, iteration, 2):
            if iteration % n == 0:
                iteration += 2
                break
        else:
            prime_numbers.append(iteration)
            iteration += 2

    print(prime_numbers)
    return len(prime_numbers)


print(count_prime_numbers(50))