class Employee:
    company = "TATA"
    def show(self):
        print(f"The name is {self.name} and the salary is{self.salary}")

#class Programmer:
#   company = "TCS"
#   def show(self):
#       print(f"The name is {self.name} and the salary is {self.salary}")
#
#   def showLanguage(self):
#       print(f"The name is {self.name} and he is good with {self.language} language")

class Programmer(Employee):
    company = "TCS" #there must be no gap after this otherwise it causes error.
    def showLanguage(self):
       print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()

print(a.company, b.company)