class Employee:
    salary = 3000000   #if you kept 30,00,000 -> becomes a tuple
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        # new salary = old salary (1 + increment/100)
        # increment = ((new salary/old salary)-1)*100
        self.increment = ((salary/self.salary)-1)*100

e = Employee()
print(f"Salary after increment: {e.salaryAfterIncrement}")
e.salaryAfterIncrement = 3600000.0
print(f"Increment of: {e.increment}%")