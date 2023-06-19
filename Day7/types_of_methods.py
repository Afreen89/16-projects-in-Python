class Bird:

    wings = True # class attribute (property)

    def __init__(self, color, species): # Instance Attribute
        self.color = color
        self.species = species

    def chirp(self): # Instance method
        print("tweet")

    def fly(self, feet): # Instance method
        print(f"The bird flies {feet} feet high")
        self.chirp() # Instance methods can also access other methods

    def paint_black(self): # Instance methods can access and change the object attributes
        self.color = "black"
        print(f"Now the bird is {self.color}")

    @classmethod
    def lay_eggs(cls, number):
        print(f"It laid {number } eggs")
        cls.wings = False # Can change class attributes but cannot access instance attributes
        print(Bird.wings)

    @staticmethod
    def look():
        print("The bird looks")

# tweetie = Bird("yellow", "cranny") # class object
#
# tweetie.paint_black()
#
# tweetie.fly(164)
#
# tweetie.wings = False # class attributes can be modified
#
# print(tweetie.wings)

Bird.look()
