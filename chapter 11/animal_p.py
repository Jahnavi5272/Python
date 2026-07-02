class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("Bow bow!")

d = Dog()
d.bark()
Dog.bark()

class Cat(Pets):                # Cat = class name
    def meowing(self, sound):   # meowing = method
                                # self = current object
                                # sound = parameter
        print(sound)            # sound = variable

m = Cat()                       # m = object
m.meowing("Meow meow")          # meow = value -> argument

class Cow(Pets):
    def __init__(self):
        self.sound = "Deviiiii!"

    def Devi(self):
        print(self.sound)

c = Cow()
c.Devi()