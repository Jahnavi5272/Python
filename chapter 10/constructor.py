class Employee:
    language = "Pyhton"
    salary = 1200000

    # __new__ => object creation
    def __init__(self, name, salary, language):    # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object.")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Good morning!")

janu = Employee("Janu", 5000000, "Java")
# janu.name = "Janu"
print(janu.name, janu.salary, janu.language)

#amu = Employee()