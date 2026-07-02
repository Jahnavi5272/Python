#print 3rd, 5th, 7th elements from the list
l = [1, 2, 3, 4, 5, 4, 7, 6, 9, 10]
#for i in range (len(l)):
#    print(f"{2* l[i] + 1}")

# here i is the index. ij n
for i, item in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(item)