 #Nicholas Soluri
 #CSC 111 Dr. Burhans
 #loops.py Lab 7 Due 10/17/18


print()
print()
print('***** problem 1 *****')
print('***** while *****')
print()

    
numcaps = 0
numspace = 0
sent = input('Please give me a sentence!: ')
index = 0
while index < (len(sent)):
    
    if sent[index] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
         numcaps +=1
    elif sent[index] == ' ':
        numspace +=1

    index +=1
     
print('There are', numcaps, 'capital letter(s) and', numspace, 'space(s) in your sentence')

print()
print()
print('***** problem 2 *****')
print('***** for...in *****')
print()

for i in range(-10, 61, 5):
    print(i)

print()
print()
print('***** problem 3 *****')
print('***** for...in *****')
print()


mylist = [7,4,5,6,1,2,3]

maxval = mylist[0]
for val in range(len(mylist)):
    if val < maxval:
        maxval = maxval
    elif val > maxval:
        val = maxval
print(maxval)
print()
print()
print('***** problem 4 *****')
print('***** for...in *****')
print()

mylist = [2,4,6,8,3,5,7]
index = 0
for i in range(3):
    num = int(input('type a number: '))
    if num in mylist[0:]:
        if num == 2:
            index = 0
            print('number is in the list at position', index)
        elif num == 4:
            index = 1
            print('number is in the list at position', index)
        elif num == 6:
            index = 2
            print('number is in the list at position', index)
        elif num == 8:
            index = 3
            print('number is in the list at position', index)
        elif num == 3:
            index = 4
            print('number is in the list at position', index)
        elif num == 5:
            index = 5
            print('number is in the list at position', index)
        elif num == 7:
            index = 6
            print('number is in the list at position', index)
    else:
        print('sorry it is not here')



print()
print()
print('***** problem 5 *****')
print('***** for...in *****')
print()
list7 = []
sum1 = 0
for i in range(7):
    value = float(input('give me a decimal: '))
    list7.append(value)
    sum1 = sum1 + value
print(list7)
print('the sum of these values is', sum1)                 



print()
print()
print('***** problem 6 *****')
print('***** for...in *****')
print()

for row in range(1,9):
    for col in range(1,9):
        print('(',row,',',col,')')
    


print()
print()
print('***** problem 7 *****')
print('***** while *****')
print()



name = input('what is your name?: ')
item  = input('what do you want to bring to the moon? Type stop to quit: ')

while (len(item) > 0) and item != '' :
    if ((item[0] == name[0]) or (ord(item[0]) == (ord(name[0]) + 32))):
        print('you can bring (a/an)', item, '!')
    elif item[0] != name[0]:
        print('You cannnot bring (a/an)', item, '!')
    item = input('what else do you want to bring?: ')
        















