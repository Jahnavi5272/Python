class Employee:
    a = 100

    @classmethod
    def show(cls):
        print(f"The class attribute is {cls.a}")

e = Employee()
e.a = 50
e.show()