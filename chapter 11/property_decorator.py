class Employee:
# we have packed many working components in a single unit, it's called encapsulation.
    a = 100

    @classmethod
    def show(cls):
        print(f"The class attribute is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
        # here we are not showing implementation details so it's called abstraction.

e = Employee()
e.a = 50
e.name = "John Leo"
print(e.name)
print(e.fname, e.lname)
e.show()