# Nicholas Soluri
# Lab 3 9/12/18
# Length.py
# CSC 111

# this program will count the length of a sequence of characters
# below, the favorite word is input by the user

mystring = input('type your favorite word: ')
count = 0

for item in mystring:
    print(item)
    count = count + 1
# a sentence displayoing the length of the favorite word is  now printed below

print('Your favorite word', mystring, 'is', len(mystring), 'letters long')
    
