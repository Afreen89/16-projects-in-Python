class Animal:

    def __init__(self, age, color):
        self.age = age
        self.color = color

    def born(self):
        print("This animal has been born")

    def Talk(self):
        print("This animal makes a sound")


class Bird(Animal):

    def __init__(self, age, color, altitude):
        super().__init__(age, color)
        self.altitude = altitude
    def Talk(self):
        print('chirp')

    def fly(self, feet):
        print(f"This bird flies {feet} feets")

# print(Bird.__bases__)
# print(Animal.__subclasses__() )

tweetie = Bird(2, 'yellow', 196)
# print(tweetie.color)
# tweetie.born()
# tweetie.Talk()

tweetie.Talk()

