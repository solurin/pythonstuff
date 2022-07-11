# vowel.py
# Nicholas Soluri
# Planning to Code 10/3/18
# CSC 111 Dr. Burhans

word = input('give me a word: ')
numV = 0
vowels = 'aeiouAEIOU'

if word[0] in 'Yy':
    if len(word) > 1 and word[1] not in vowels:
        vowels +=1
    elif len(word) == 1:
        vowels +=1
    
        
index = 0
while index <= len(word) and word[index] in vowels:
    numV +=1
    index +=1
    
print('There are', numV, 'vowels at the start of the word.')
print('starting vowel(s):', word[0:numV])
if numV == 0:
    print('no vowels at the start')
            
            
    

