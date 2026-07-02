# Remove a given word from a list and strip it at the same time

# This is used for removing the word
#def rem(l, word):
#    for item in l:
#        l.remove(word)
#        return l
#
#l=["Janu", "Amu", "Swathi", "Chalam", "anu"]
#print(rem(l, "anu"))

# This is used for stripping the word

def rem(l, word):
    n = []
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l=["Janu", "Amu", "Swathi", "Chalamu", "anu", "umbrella", "reach", "anti"]
print(rem(l, "anu"))