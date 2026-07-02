class Vector:
    def __init__(self, d, e, f):
        self.d = d
        self.e = e
        self.f = f

    def __add__(self, new):
        result = Vector(self.d + new.d, self.e + new.e, self.f + new.f)
        return result

    def __mul__(self, new):
        result = self.d * new.d + self.e * new.e + self.f + new.f
        return result

    def __str__(self):
        return f"Vector {self.d}, {self.e}, {self.f}"

v1 = Vector(3,8,9)
v2 = Vector(2,5,7)
v3 = Vector(1,4,6)

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)