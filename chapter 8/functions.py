# Function definition
# def avg():
#     a = int(input("Enter the value of a: "))
#     b = int(input("Enter the value of b: "))
#     c = int(input("Enter the value of c: "))
#
#     average = (a +b + c)/3
#     print(average)
#
# avg()

#def goodDay(name, ending):
#    print("Good Day " + name)
#    print(ending)
#goodDay("Janu", "Thank you")
#goodDay("Amu", "Thanks")

def greet(name):
    print("This is a greet function")
    gr = "Hello " + name
    return gr #if it's not there then it will print none
a = greet("Janu")
print(a) #if it's not there then it will print the 1st line only.