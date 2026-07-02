with open("log.txt", "r") as f:
    content = f.read()

if "python" in content:
    print("Yes python is present.")
else:
    print("No pyhton is not present.")