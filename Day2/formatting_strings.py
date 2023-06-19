x = 10
y = 5

print("My numbers are " + str(x) + " and " + str(y))
print("My numbers are {} and {}".format(x, y))
print("The sum of {} and {} is equal to {}".format(y, x, y+x))

####################################################

color = "red"
license_plate = 543645

print(f"The car is {color} and its license plate is {license_plate}")

# Exercise
previous_points = 875
new_points = 350

print("You have earned {} points! In total, you have accumulated {}".format(new_points, previous_points + new_points))