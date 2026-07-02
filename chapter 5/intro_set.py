#s = {1,2,3,4,5,6,7,8,9,0,0,0,0,0,"Janu"}
#print(s, type(s))
#s.add(23)
#print(s)

s1={1,2,3,4,5}
s2={9,8,7,6,5,12}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.issubset(s2))
print(s1-s2)
print(s2.difference(s1))