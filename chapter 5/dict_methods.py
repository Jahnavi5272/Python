marks = {
    "Janu": 100,
    "Priya": 98,
    "Sireesha": 83,
    0: "Harry"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Janu": 105, "Jahnavi": 100})
print(marks)
print(marks.get("Janu2")) #prints None
print(marks["Janu2"]) #prints an error