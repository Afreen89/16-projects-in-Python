def addition():
    n1 = int(input("The first number: "))
    n2 = int(input("The second number: "))
    print(n1 + n2)
    print("Thanks for adding" + n1)

try:
    addition()

except TypeError:
    print("You are trying to concatenate different types")

except ValueError:
    print("This is not a number")

else:
    print("You did great")

finally:
    print("That's all!")