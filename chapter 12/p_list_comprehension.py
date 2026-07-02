# print list containing tables of entered number.
n = int(input("Enter a number: "))
table = [n*i for i in range(1, 11)]
for i in range(1,11):
    print(f"{n} * {i} = {table[i-1]}")