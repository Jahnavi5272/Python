# finally are used when we are in function.
# if I took away the finally then that print statement will not be executed.
def main():
    try:
        a = int(input("Enter a number:"))
        print(a)
        return
    except ValueError as v:
        print(v)
        return
    finally:
        print("I am inside finally.")

main()