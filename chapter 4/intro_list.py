a = ["Apple", "string", 8, 3.14, True, "Why"]
l1 = [1,2,3,47,23,9,67,12,5]
#sorting
#l1.sort()
#print(l1)

#reverse
l1.sort(reverse=True)
print(l1)
l1.reverse()
print(l1)

#pop
value = l1.pop(3)
print(value)
print(l1)

#remove
l1.remove(23)
print(l1)