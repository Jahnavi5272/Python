class Employee:
    language = "Pyhton"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")

    @staticmethod   #will not use self.
    def greet():
        print("Good morning!")

janu = Employee()
#janu.language = "JavaScript"  # This is an instance attribute.
janu.greet()
janu.getInfo()
#Employee.getInfo(janu)