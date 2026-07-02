class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer")
    b = 21

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 89

#o = Employee()
#print(o.a)

#o = Programmer()
#print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)