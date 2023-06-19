name = input("What is your name? ")
sales = int(input("How much sales have you done this month? "))
sales = round(0.13 * sales, 2)

print("Ok {}, This month you won ${}".format(name, sales))

print(f"Ok {name}, This month you won ${sales}.")
