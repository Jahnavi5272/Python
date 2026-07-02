# c/5 = (f-32)/9

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c,3)} Degree C")


def c_to_f(c):
    return (c*9/5)+32

c = float(input("enter temperature in C: "))
print(f"{c_to_f(c)} F")