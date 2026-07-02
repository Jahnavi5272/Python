class Employee:
    language = "Python" #This is a class attribute
    salary = 2400000

class employee:
    work = "Embedded Systems Engineer"
    salary = 3000000

janu = Employee()
janu.name = "Jahnavi"   #This is an instance attribute.
print(janu.name, janu.language, janu.salary)

amu = employee()
amu.name = "Amani"
print(amu.name, amu.salary, amu.work)

# name is object attribute or instance attribute
# age and salary are class attributes as they directly belong to class.