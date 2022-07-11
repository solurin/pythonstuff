# iterator loops
# Lab 7 October 10
# Dr. Burhans
# Nicholas Soluri
#iteration happens over collections of things
# so far: lists, sets, tuples, strings, dictionaries

#iterate over a string and print the letters one per line
# delivers up, binds each element in a collection in turn to a loop variable
# goes through one element at a time until all have been gone through
for letter in 'hello why is Buffalo so hot?':
    print(letter)
# how many times did this iterator run?
count = 0
for letter in 'hello why is Buffalo so hot?':
    print(letter)
    count = count + 1

print('the iterator ran', count, 'times')
print('my string: hello why is Buffalo so hot?')
print('length of string is', len('hello why is Buffalo so hot?'))

# create and iterate over a set
myset = ('dog', 'cat', 'bird', 'cow')
for animal in myset:
    print(animal)
    
# create and iterate over a tuple
mytuple = ('this', 'that', 'then', 42)
for item in mytuple:
    print(item)

# create and iterate over a dictionary
mydict = {'dog': 'bark', 'cat': 'meow', 'bird':50, 'cow': (2,3,4)}
for key in mydict:
    # use key as index
    print(key, mydict[key])
    
# now we will do something bad
# now we will jump out of the iterator before it's time and
# before its time
mystring = 'what the heck'
for ch in mystring:
    if ch == 'e':
        print('arggh undisciplined loop exit')
        break


# instead if you have a condition for ditching iteration, use a while loop
# use a while loop like this!!!!!
index = 0
while index < len(mystring) and mystring[index] != 'e':
    print(mystring[index])
    index +=1
if index < len(mystring):
    print('e found at location', index)






