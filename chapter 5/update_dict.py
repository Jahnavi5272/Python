d = {}

name = input("Enter your name: ")
lang = input("Enter your language: ")
d.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter your language: ")
d.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter your language: ")
d.update({name:lang})

#as we are updating the names, if we wrote same name for 2 keys then the 2nd value will be taken
#it's different for values, they get printed even if we write many times
print(d)