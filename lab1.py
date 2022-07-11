#Nick Soluri
#Dr. Meyer CSC 112
#Lab 1 Due Jan 23 2019


#i was unable to download main.py and infiniteint3.py as they were no longer
#on D2L




def subtract(num, num2):
    
    for i in range(len(tempmystring)):
        digit1 = int(tempmystring[i])
        digit2 = int(otherstring[i])
        if digit1 - digit2 - borrow < 0:
            newdigit = digit1 + 10 - digit2 - borrow
            borrow = 1
        else:
            newdigit = digit1 - digit2 - borrow
            borrow = 0
        newstring += str(newdigit)
