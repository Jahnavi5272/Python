import re

with open("replace_update_letter.txt", "r") as f:
    content = f.read()

content = re.sub(r"[aeiou]", "*", content, flags=re.IGNORECASE)

with open("replace_update_letter.txt", "w") as f:
    f.write(content)