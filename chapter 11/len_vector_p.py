class Vector:
    def __init__(self, l):
        self.l = l

    def __len__(self):
        return len(self.l)

v1 = Vector([8,4,7,7])
print(len(v1))