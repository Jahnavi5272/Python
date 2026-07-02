# in python its try and except
# in c, c++, JavaScript its try and catch

try:
    n = int(input("Enter a number: "))
    print(n)

except Exception as e:
    print(e)

else:
    print("As try is executed successfully, so now i am inide else")

# if try gets executed then else will also get executed.