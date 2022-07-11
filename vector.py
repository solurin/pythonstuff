# Nicholas Soluri
#CSC 111 Lab 9: Functions and Loops in a menu-driven system
#10/24/18

'''
     Nicholas Soluri
    CSC 111 Lab 9: Functions and Loops in a menu-driven system
    10/24/18

'''

##### import statements #####
import math





##### function definitions #####
def largestVal(v1, v2):
    '''
        find the highest value in each vector
        parameters: v1, v2
        returns: none

    '''
    print('the largest value in v1 is', max(v1), 'and the largest value in v2 s', max(v2))














def magnitudes(v1, v2):
    '''
        find the square root of sum of squares of each position of each list
        parameters: v1, v2
        returns: none
    '''
    index = 0
    sumlist1 = []
    sumlist2 = []
    while index < len(v1):
        val1 = (v1[index] ** 2)
        sumlist1.append(val1)
        index +=1

    index = 0
    sumlist2 = []
    while index < len(v2):
        val2 = (v2[index] ** 2)
        sumlist2.append(val2)
        index +=1


    mag1 = math.sqrt(sum(sumlist1))
    mag2 = math.sqrt(sum(sumlist2))
    print('the magnitude of v1 is', mag1, 'and the magnitude of v2 is', mag2)











def dotProduct(v1, v2):
    '''
        find the product of each postion value of each vector
        print the dot product
        paramters: v1, v2
        returns: none
    '''
    index = 0
    prodlist = []
    while index < len(v1):
        dotproddy = (v1[index]) * (v2[index])
        prodlist.append(dotproddy)
        index +=1
        

    print('the dot product of v1 and v2 is', (sum(prodlist)))











def addVectors(v1, v2):
    '''
        add the values at each corresponding position in each vector and
        print the list which contains the sums at each position
        parameters: v1, v2
        returns: none
    '''
    index = 0
    sumlist = []
    while index < len(v1):
        val = v1[index] + v2[index]
        sumlist.append(val)
        index +=1

    print('the sum of the vectors is: ', sumlist)






def vecDim(v1, v2):
    '''
        print the dimensionality (length of the list) for each vector
        parameters: v1, v2
        returns: none
    '''
    print('the dimensionality of the vectors is', len(v1))





def printVectors(v1, v2):
    '''
        print the vectors input from the user
        parameters: v1, v2
        returns: none
    '''
    print('vector 1:', v1, 'vector 2:', v2)
    



def getVectors():
    '''
        get the vectors lists from the user
        parameters: none
        returns: two lists representing the values
    '''
    v1 = []
    v2 = []
    # while loop that gets values and adds to v1 until the user types
    # a value <= -1000 note: convert all values to float

    val = float(input('type a value, <= -1000 to quit: '))
    while val > -1000:
        v1.append(val)
        val = float(input('type a value, <= -1000 to quit: '))


    #now use a for range loop to get values for v2
        # why? the length of v1 is the number of values you need to
        # input for v2 because they have to be the same length

    for i in range(len(v1)):
            #need to get a value and append it to v2
        val = float(input('type a value: '))
        v2.append(val)

    return v1, v2










def main():
    '''
        creates a menu for users to select various choices from
        runs the prgoram, uses no paramters
    '''
    v1 = []
    v2 = []
    while True:
        print('Welcome to vector arithmetic! Below is a list of operations. \n')
        print('Select a choice from the following\n')
        print('\t1. Enter values for your vectors')
        print('\t2. Print vectors')
        print('\t3. Vector dimensionality')
        print('\t4. Add vectors')
        print('\t5. Compute dot product of vectors')
        print('\t6. Compute magnitude of vectors')
        print('\t7. Largest value in each vector')
        print('\t8. Quit')

        choice = int(input('Type number for selected operation: '))
        print()
        if choice == 8:
            break
        elif choice == 1:
            
            v1, v2 = getVectors()
            pass
        elif choice == 2:
            printVectors(v1, v2)
            pass
        elif choice == 3:
            vecDim(v1, v2)
            pass
        elif choice == 4:
            addVectors(v1, v2)
            pass
        elif choice == 5:
            dotProduct(v1, v2)
            pass
        elif choice == 6:
            magnitudes(v1, v2)
            pass
        elif choice == 7:
            largestVal(v1, v2)
            pass
        else:
            print('Invalid choice, choose again\n')





##### main program code #####
main()
