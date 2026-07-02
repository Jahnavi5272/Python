import re
words = ["Jahnavi", "Amani", "Swathi", "Chalam"]

with open("replace_update_many.txt", "r") as f:
    content = f.read()

for word in words:
    pattern = rf"\b{word}\b"
    content = re.sub(pattern, "*" * len(word), content, flags=re.IGNORECASE)

with open("replace_update_many.txt", "w") as f:
    f.write(content)