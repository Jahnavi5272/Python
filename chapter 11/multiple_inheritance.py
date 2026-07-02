class Employee:
    company = "TATA"
    name = "Something name"
    #salary = "30 LPA"
    def show(self):
        print(f"The name is {self.name} and she is working at {self.company}")

class Coder:
    language = "Python"
    def print_language(self):
        print(f"Here is your language: {self.language}")

class Programmer(Employee, Coder):
    company = "TCS" #there must be no gap after this otherwise it causes error.
    name = "Janu"
    #language = "Java"
    def show_language(self):
        print(f"The company is {self.company} and one girl is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.print_language()
b.show_language()