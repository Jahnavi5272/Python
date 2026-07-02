n = int(input("Enter a number: "))
table = [str(n*i) for i in range(1,11)]

# horizontal
# print(table)

# vetical
# for i in table:
#   print(i)

# but there is another method for vertical using format
s = "\n".join(table)
print(s)