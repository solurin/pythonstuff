# non counting loops
# lab 7 October 10
# Dr. Burhans
# Nicholas Soluri

#search for a particular value in a collection
# for example, look for a particular letter in a string
# do this using a Boolean value to track whether we have found the letter yet
# loop either until we find it or have looked at everythng and not found it
# looked at everything means our index is no longer < len(string)

mystring = 'I wonder if I will find it?'
index = 0
sought = 'f'     # I am looking for F
# Boolean variable - we have not yet found it!
found = False

while not found and index < len(mystring):
    if mystring[index] == sought:
        found = True
    else:
        index = index + 1

if found:
    print('found it at location', index)
    print(mystring)
    print(' '*(index-1), '*')
else:
    print('sorry did not find your letter')

    
# prompt user for name
# get first letter
# ask user what they want to take to the moon
# and keep asking as long as they want to
# take begins with the same letter as their name

name = input('what is your name?')
item  = input('what do you want to bring to the moon?')

while len(item) > 0 and item[0] == name[0]:
    print('nice!')
    item = input('what else do you want to bring?')
    
