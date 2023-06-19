"""
You must create a list with values and call it secret_codes.
Create a function called toss_coin that returns the result of a random coin toss.
Such a function must be able to return the results "Heads" or "Tails", and must not receive any arguments to work.
Create a second function called luck, that takes two arguments: the first must be the result of the coin toss.
The second argument will be any list (the secret_codes variable that was created at the beginning).
If the coin comes up "Tails", luck should print this message to the user: "List will self-destruct",
and return said list as empty list = [ ]. If the coin comes up "Heads", it should print to the screen: "List was saved"
and return the list intact.
Hint: Use the random library's choice method to choose an element at random from a sequence.
"""
from random import choice

secret_codes = [1, 3, 4, 6]
def toss_coin():
    my_coin = int(choice(range(0, 2)))
    if my_coin == 0:
        return "Tails"
    elif my_coin == 1:
        return "Heads"

# print(toss_coin())

def luck(coin, list1):
    if coin == "Tails":
        print("List will self-destruct")
        del list1[:]
        return list1
    elif coin == "Heads":
        print("List was saved")
        return list1

chance = toss_coin()
luck(chance, secret_codes)