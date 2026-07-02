n = int(input("Enter a number: "))

def pattern(n):
    if n==0:
        return
    print("*" * n)
    pattern(n-1)

pattern(n)
#because of adding print we get 'none' at last.