class Print:

    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j} + {self.k}k"

vector = Print(7, 8, 10)
print(vector)