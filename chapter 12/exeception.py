try:
    a = int(input("Hello, enter a number: "))
    print(a)

except Exception as e:
    print(e)

print("Please come again later")

# we also have different types of exceptions like:
# ZeroDivisionError, ValueError etc...