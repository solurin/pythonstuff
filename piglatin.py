#Nicholas Soluri
#Lab 4B
#CSC 111 Dr. Burhans
#9/19/18
 
text = input('Type a word:')
if text[0] in 'aeiouAEIOU':
    print(text + 'way')
elif text[0] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'  and text[1] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[2] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[3] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
    print(text[4:] + text[0:4] + 'ay')
elif text[0] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[1] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[2] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
    print(text[3:] + text[0:3] + 'ay')
elif text[0] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[1] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
    print(text[2:] + text[0:2] + 'ay')
elif text[0] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
    print(text[1:] + text[0:1] + 'ay')



