def ask_number():

    while True:

        try:
            number = int(input("Enter a number: "))

        except:

            print("This is not a number")

        else:
            print(f"You have entered number {number}")
            break

    print("Thank you")

ask_number()