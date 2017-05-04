from character_count import *
from string import *
def alice_counts(char):

    """
    """

    file = open("alice_in_wonderland.txt", "r")
    print(file) 
    ln = [0] * 256
    charcount = 0
    for line in file:
        ln = char_counts(line)
        charcount += ln[ord(char)]
    return "There are {0} {1}'s in Alice in Wonderland".format(charcount, char)

def alice_letts(): #just for fun
    file = open("alice_in_wonderland.txt", "r")
    lettlist = ""
    alpha = lowercase[0:25] #I need a list of the alphabet
    print(alpha)
    for lett in alpha:
        lettlist += alice_counts(lett) + "/n"
    return lettlist


#Testing alice_letts
#print(alice_letts())
#need a lsit of the alphabet    
#Testing IOWrapper printing bullshit
alice_counts("/")

#Testing the alphabet here
print(alice_counts("a"))
print(alice_counts("b"))
print(alice_counts("c"))
print(alice_counts("d"))
print(alice_counts("e"))
print(alice_counts("f"))
print(alice_counts("g"))
print(alice_counts("h"))
print(alice_counts("i"))
print(alice_counts("j"))
print(alice_counts("k"))
print(alice_counts("l"))
print(alice_counts("m"))
print(alice_counts("n"))
print(alice_counts("o"))
print(alice_counts("p"))
print(alice_counts("q"))
print(alice_counts("s"))
print(alice_counts("t"))
print(alice_counts("u"))
print(alice_counts("v"))
print(alice_counts("w"))
print(alice_counts("x"))
print(alice_counts("y"))
print(alice_counts("z"))

#Testing other characters
print(alice_counts("/"))
print(alice_counts("'"))
print(alice_counts("("))
print(alice_counts(")"))
print(alice_counts("-"))
print(alice_counts("?"))
print(alice_counts("!"))
print(alice_counts("."))
