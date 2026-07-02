f = open("file.txt")
print(f.read())
f.close()

# similar to
with open("file.txt") as f: #This is called a context manager.
    print(f.read())

# You don't have to explicitly close the file.