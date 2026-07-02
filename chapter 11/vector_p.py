class TwoDVector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"The vectors are {self.x}i and {self.y}j")

class ThreeDVector(TwoDVector):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        print(f"The vectors are {self.x}i, {self.y}j and {self.z}k")

a = TwoDVector(3,8)
a.show()
b = ThreeDVector(3,8,9)
b.show()