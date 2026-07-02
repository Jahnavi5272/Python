'''
# read a file
f = open("file.txt")
data = f.read()
print(data)
f.close()

# write a file
st = "This is a string"
f = open("myfile.txt", "w")
f.write(st)
f.close()

# read lines
f = open("file.txt")
lines = f.readlines()
print(lines, type(lines))
f.close()

# read line
f = open("file.txt")
line1 = f.readline()
print(line1, type(line1))
line2 = f.readline()
print(line2, type(line2))
line3 = f.readline()
print(line3, type(line3))
line4 = f.readline()
print(line4, type(line4))
line5 = f.readline()
print(line5 == "")
f.close()
'''

# read line using while
f = open("file.txt")
line = f.readline()
#while line is not equal to empty string
while line != "" :
    print(line)
    line = f.readline()   #helps in updation.
f.close()