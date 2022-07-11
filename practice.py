practice


print elements of a list/string/whatever in reverse order


var = 'hello how are you'
index = (len(var)-1)

while index >= 0:
    print(var[index])
    index -= 1


create a 3rd list that is the quotient of the first list divided by
 the second list at the same position

list1 = [10, 20, 30, 40, 50, 60, 70]
list2 = [2, 5, 10, 4]
list3 = []
index = 0


while index < len(list2):
    list3.append(list1[index] / list2[index])
    index +=1
while index < len(list1):
    list3.append(list1[index])
    index +=1
print(list3)

 create a function thta condenses a string: if there are multiple spaces
 consecutively, make it one

def condense(string):
    newstring = ''
    index = 0
    while index < len(string):
        if string[index] != ' ':
            newstring = newstring + string[index]
            index +=1
        elif string[index] == ' ' and string[index + 1] != ' ':
            newstring = newstring + string[index]
            index +=1
        elif string[index] == ' ' and string[index + 1] == ' ':
            index +=1
    
    return newstring
string = 'i     love    this class!'
print(condense(string))



 find the smallest and second smallest values in a list


nums = [5, 3, 7, 4, 6, 56, 100, 76, 8, 4, 9, 234, 4, 2, 6]

index = 1
smallest = nums[0]

while index < len(nums):
    if nums[index] < smallest:
        smallest = nums[index]
        index +=1
    else:
        index +=1

index = 0
newnums = []
while index < len(nums):
    if nums[index] != smallest:
        newnums.append(nums[index])
        index +=1
    else:
        index +=1

         
index = 1
secsmall = newnums[0]
while index < len(newnums):
    if newnums[index] < secsmall:
        secsmall = newnums[index]
        index +=1
    else:
        index +=1

print(nums)
print('The smallest number in this list is', smallest, 'and the second smallest number is', secsmall)



for num in range(19, 10, -2):
    print(num)


petstore = {'cat': 8, 'dog': 9}

print(petstore)


if 'dog' in petstore:
    print("True")
else:
    print('False')


petstore = {'emu': 4, 'dog': 6, 'cat': 8}
if 'emu' in petstore:
    print(petstore['emu'])
else:
    print('sorry not found')
    



import math

def powten(x):
    index = 0
    while (10 ** index) <= x:
        if 10 ** index != x:
            index +=1
        elif 10 ** index == x:
            print(x, 'is a power of 10')
            break

print(powten(1000))















