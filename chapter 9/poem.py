your_input = input("Enter the word you want to find: ")
f = open("poem.txt")
content = f.read()
if your_input.lower() in content.lower():
    print("The word is in the poem.")
else:
    print("The word is not present in the poem.")
f.close()