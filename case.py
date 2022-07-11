#Nicholas Soluri
# 9/19/18 Lab 4 CSC 111
#case.py
#to determine how many lowercase, capital, ad nonletters there are in an input
intext = input('Type something:')
#set counts for letter and nonletter to 0
countofcaplet = 0
countoflowlet = 0
countofnonlet = 0
for ch in intext:
    
    if ch>= "A" and ch<= "Z":
        countofcaplet +=1
    if ch >= 'a' and ch<= 'z':
            countoflowlet +=1
    else:
        countofnonlet +=1
        
print('There are', countofcaplet, 'capital letters in your input.')
print('There are', countoflowlet, 'lowercase letters in your input.')
print('There are', countofnonlet, 'nonletters in your input.')
