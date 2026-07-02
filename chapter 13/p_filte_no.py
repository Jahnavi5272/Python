l = [1,2,5,10,46,25,60,34,35,8]
def divisible(n):
    return n%5==0

for n in l:
    if divisible(n):
        print(n)