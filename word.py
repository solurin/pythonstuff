# word.py
# Nicholas Soluri
# Planning to Code 10/3/18
# CSC 111 Dr. Burhans

numcaps = 0
numspace = 0
sent = input('Please give me a word: ')
index = 0
while index < (len(sent)):
    
    if sent[index] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
         numcaps +=1
    elif sent[index] == ' ':
        numspace +=1

    index +=1
     
print('There are', numcaps, 'capital letters and', numspace, 'spaces in your sentence')
    



