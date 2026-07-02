import re
with open("replace_update.txt", "r") as f:
    content = f.read()

content = re.sub(r"jahnavi", "Janu", content, flags=re.IGNORECASE)
        # re = regex
        # sub = substitute
        # r = raw string

with open("replace_update.txt", "w") as f:
    f.write(content)