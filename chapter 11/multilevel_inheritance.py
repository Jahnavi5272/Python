class Employee:
    a = 1

class Programmer(Employee):
    b = 21

class Manager(Programmer):
    c = 89

o = Employee()
print(o.a)

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)