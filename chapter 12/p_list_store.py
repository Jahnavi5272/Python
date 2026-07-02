import os
print("File location: ",os.getcwd())
n = int(input("Enter a number: "))
table = [f"{n} * {i} = {n*i}" for i in range (1,11)]
with open("p_table.txt", "a") as g:
    g.write("\n")
    g.write(f"{n} table is: \n")
    g.write("\n".join(table))