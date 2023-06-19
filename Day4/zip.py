names = ["Hanna", "Bruce", "Tony"]
ages = [65, 29, 43, 55]
cities = ["New York", "London", "Berlin"]

combination = list(zip(names, ages, cities))
for name, age, city in combination:
    print(f"{name} is {age} years old and lives in {city}")