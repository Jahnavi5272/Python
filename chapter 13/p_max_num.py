"""
find max without reduce
l = [1,45,78,34,89,23,68,35,8]
def greater(l):
    greatest = l[0]
    for n in l:
        if n > greatest:
            greatest = n
    print(greatest)

greater(l)
"""

# max number using reduce
# checks every two elements
from functools import reduce
l = [1,45,78,34,89,23,68,35,8]
def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))