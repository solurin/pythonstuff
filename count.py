#counting loops
# Lab 7 October 10
# Dr. Burhans CSC 111
# Nicholas Soluri

# input a number from the user
# positive integer
# print 'hello' that many times
# original prompt with no enclosing while
# num = int(input('type a positive integer: '))

# make into a nested loop with while around it
# that tells user to typer a number < 0 to quit
# initialization - num is the loop variable

num = int(input('type a number >= 0, <0 to quit: '))
# condition is num >= 0
# means as long as num >= 0 go into the loop
# when num NOT >= 0 do not go into the loop, move on to next statement
# if there is not one, it is the end of the program
while num >= 0:
    #body contains two statements:
    # for in range loop; assignment statement
    # i is loop variable, automatically initialized in this form of range loop
    # 0. condition is i < num --- automatic
    # update happens automatically and this form adds 1 to the loop variable


    for i in range(num):
        print(i, 'hello')
    # UPDATE of loop variable   
    num = int(input('type a number >= 0, <0 to quit: '))

    
#experiment with infinite counting loop
#will comment out after running once
#never stops --- missing update
# to stop --- ctrl + c
##count = 0
##while count < 10:
##    print('in loop and count is', count)
##
##    #update is missing


# make another infinite loop where comparison will never be true
# based on initialization and update
##count = 0
##while count != 10:
##    print('count is', count)
##    count = count - 1

#what is wrong with this loop?
# update does not bring the loop variable closer to the test and it will never
# reach the test

#use a while to count up through 100 and print the odd numbers starting from 0

# solution 1: generate all numbers from 0-100 (inclusive)
    # test if odd, if so, print
num = 0
while num <= 100:
    if (num % 2) == 1:
        print(num)
    num +=1
#soluion 2: start with 1, count by 2. all numbers will be odd
    # will be 50 numbers
num = 1
while num <= 100:
    print(num)
    num +=2

