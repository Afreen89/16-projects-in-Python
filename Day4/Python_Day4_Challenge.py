import random
# from random import random
from random import randint
from random import choice
user_name = input("Please, enter your full name? ")
print(f"Well {user_name}, I have thought of a number between 1 and 100 and you have only eight tries to guess it.")
program_number = random.randint(1, 100)
tries = 0
my_number = 0


while tries < 8:
    my_number = int(input("What number do you think it is: "))
    tries += 1

    if my_number > 100 or my_number < 0:
        print("You have chosen a number that is out of play")
    elif my_number < program_number:
        print("You chose a lower number than the secret number")
    elif my_number > program_number:
        print("You chose a greater number than the secret number")
    else:
        print(f"You got the secret number right and it took you {tries} tries")
        break

if my_number != program_number:
    print(f"You lost! No more attempts are left. The secret number is {program_number}")
