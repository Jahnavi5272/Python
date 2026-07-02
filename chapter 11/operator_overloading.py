class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(3)
m = Number(5)

print(n+m)