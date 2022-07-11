

sent = input('give me a sentence: ')

wordlist = sent.split(' ')

index = 0



    
while index < len(wordlist):
    if wordlist[index][0] in 'aeiouAEIOU':
        print((wordlist[index] + 'yay'), end = ' ')
    elif wordlist[index][0] not in 'aeiouAEIOU' and wordlist[index][1] not in 'aeiouAEIOU' and wordlist[index][2] not in 'aeiouAEIOU' and wordlist[index][3] not in 'aeiouAEIOU':
        print((wordlist[index][4:] + wordlist[index][0:4] + 'ay'), end = ' ')
    elif wordlist[index][0] not in 'aeiouAEIOU' and wordlist[index][1] not in 'aeiouAEIOU' and wordlist[index][2] not in 'aeiouAEIOU':
        print((wordlist[index][3:] + wordlist[index][0:3] + 'ay'), end = ' ')
    elif wordlist[index][0] not in 'aeiouAEIOU' and wordlist[index][1] not in 'aeiouAEIOU':
        print((wordlist[index][2:] + wordlist[index][0:2] + 'ay'), end = ' ')
    elif wordlist[index][0] not in 'aeiouAEIOU':
        print((wordlist[index][1:] + wordlist[index][0] + 'ay'), end = ' ')
    index +=1
        
    

















        



    
