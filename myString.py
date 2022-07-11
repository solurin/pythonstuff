# Nicholas soluri
# CSC 111 Lab Dr. Burhans
# Lab 10 part 2 ---- myString.py
def count(x, string):
    index = 0
    count = 0
    while index < len(string):
        if string[index] == x:
            count +=1
            index +=1
        elif string[index] != x:
            index +=1
    return count







def rfind(x, string):
    index = 0
    revstring = string[: :-1]
    while index < len(revstring):
        if revstring[index] == x:
            return index
        elif revstring[index] != x:
            index +=1








def find3(x, start, end, string):
    index = start
    while index < end:
        if string[index] == x:
            return (index - start)
        elif string[index] != x:
            index +=1







def find2(x, start, string):
    index = start
    while index < len(string):
        if string[index] == x:
            return (index - start)
        elif string[index] != x:
            index +=1

def find(x, string):
    index = 0
    while index < len(string):
        if string[index] == x:
            return index
        elif string[index] != x:
            index +=1




print(find('f', 'physics is fun'))
print(find2('b', 4, 'I enjoy basketball'))
print(find3('g', 5, 15, 'where am I going?'))
print(rfind('r', 'alrighty'))
print(count('a', 'an apple sits at the foot of a tree'))
