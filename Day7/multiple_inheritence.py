class Father:

    def talk(self):
        print("Hello")


class Mother:

    def laugh(self):
        print("Ha ha")


    def talk(self):
        print("How are you?")

class Child(Father, Mother):
    pass


class Grandchild(Child):
    pass


my_grandchild = Grandchild()

# my_grandchild.talk()

print(Grandchild.__mro__)