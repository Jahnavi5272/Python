l = [1,2,5,10,46,25,60,34,35,8]
def divisible(n):
    if(n%5==0):
        return True
    else:
        return False

div_by_five = list(filter(divisible, l))
print(div_by_five)  # requires => return True to get printed