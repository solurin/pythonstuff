# Nicholas Soluri
# Lab 8 - Functions
# CSC 111 Dr. Burhans
# Due 10/24/18
# funk.py

####### function definitions ########
def letter(mystring):
    '''
        This function takes in a string, if it starts with a letter
        return a two letter string with both the upper and lower case versions
        of that letter. Otherwise return the empty steing.
        Parameters: string
        Returns: string
    '''
    retval = ''
    if mystring[0] >= 'A' and mystring[0] <= 'Z':
        #upper case letter
        retval = mystring[0] + chr(ord(mystring[0]) + 32)
    elif mystring[0] >= 'a' and mystring <= 'z':
        #lower case letter
        retval = chr(ord(mystring[0]) - 32)  + mystring[0] 

    return retval


def smallest(mylist):
    '''
        Takes a list and returns the smallest value
        paramters: one list
        returns: smallest value from list
    '''
    
    n=0
    smallestval = mylist[0]
    index = mylist[n]
    
    while n < len(mylist):
        if mylist[n] < smallestval:
                smallestval = mylist[n]
                smalestval = index
        n +=1
    
    return smallestval      
    

def smaller(pair):
    '''
        take two numbers and return the smaller of the two values
        Parameters: the pair of numbers
        return: the lesser value
    '''

    if pair[0] > pair[1]:
        return pair[1]
    else:
        return pair[0]
    
def numbers(sent):
    '''
        Take a string and move all of the numbers in the string into a
        list.
        Parameters: the string
        return: a list containing all of the numbers
        present in the list
    '''
    digits = '0123456789'
    nums = []
    index = 0
    while index < len(sent):
        if sent[index] in digits:
            num = sent[index]
            index +=1
            while index < len(sent) and sent[index] in digits:
                num = num + sent[index]
                index +=1
            nums.append(num)
        else:
            index +=1
    intnums = []
    for num in nums:
        intnums.append(int(num))
    return intnums
    



def piglatin(sent):
    '''
        this function will be used to translate an entire sentence (string) into
        piglatin.
        parameters: the sentence
        return: the sentence translated into piglatin
    '''
    pl = []
    words = sent.split()
    index = 0
    while index < len(words):
        for text in words:
            if text[0] in 'aeiouAEIOU':
                text = (text + 'way')
                pl.append(text)
                index +=1
            elif text[0] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'  and text[1] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[2] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[3] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
                text = (text[4:] + text[0:4] + 'ay')
                pl.append(text)
                index +=1
            elif text[0] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[1] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[2] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
                text = (text[3:] + text[0:3] + 'ay')
                pl.append(text)
                index +=1
            elif text[0] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[1] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
                text = (text[2:] + text[0:2] + 'ay')
                pl.append(text)
                index +=1
            elif text[0] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
                text = (text[1:] + text[0:1] + 'ay')
                pl.append(text)
                index +=1
    
    plstring = str(pl[0:])

    return plstring












print('Sent:823', 'Returned :', letter('823'))
print('Sent: This', 'Returned :', letter('This'))
print('Sent: and', 'Returned :', letter('and'))
mylist = [9,2,0,3]
print('Sent: [9,2,0,3]', 'Returned:', smallest(mylist))
mylist = [100]
print('Sent: [100]', 'Returned:', smallest(mylist))
mylist = [5,5,5]
print('Sent: [5,5,5]', 'Returned:', smallest(mylist))
pair = [100,4]
print('Sent: [100,4]', 'Returned: ', smaller(pair))
pair = [0,15]
print('Sent: [0,15]', 'Returned: ', smaller(pair))

print('Sent: I have 18 cats and 742 friends, one is named B3n.',)
print('Returned:',numbers('I have 18 cats and 742 friends, one is named B3n.'))
      
print('Sent: I have 18 with 742 friends, one is named B3n.', 'Returned:', numbers('I have 18 with 742 friends, one is named B3n.'))
print('Sent: Hello my name is Nicholas.', 'Returned:', numbers('Hello my name is Nicholas.'))
print('Sent: 1 2 3 4 5 ', 'Returned:', numbers('1 2 3 4 5 .'))
print('Sent: 12 134 1567', 'Returned:', numbers('12 134 1567.'))




       




        
    

print('Sent: this is a sentence')
print('Returned:', piglatin('this is a sentence'))
print('Sent: what is going on')
print('Returned:', piglatin('what is going on'))
print('Sent: hello how are you')
print('Returned:', piglatin('hello how are you'))
    
