# Nicholas Soluri
# CSC 111 Lab 3 9/12/18
# ave.py

# in this program, a the number of integers, sum, and average of a list
    # will be calculated and printed

#the list below was created by me (the programmer) and was NOT iput by the user
    #as there is no input prompt for the list of integers

mylist = [1,2,3,4,5,6]
sum = 0
count = 0

for item in mylist:
    count = count + 1
    sum = sum + item

ave = (sum/6)

# below is where the information will be presented to the user

print(mylist)
print('The sum of these numbers is', sum)
print('There are', count,  'numbers in this list')
print('the average of these values is', ave)

    
    
