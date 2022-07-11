#Nicholas Soluri
#CSC 111 Dr. Burhans
#9/26/18
#piglat.py


text = input('Type a word:')
while text != '0':
    if text[0] in 'aeiouAEIOU':
        print((text), 'translates to', text + 'way')
    elif text[0] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'  and text[1] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[2] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[3] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        print((text), 'translates to', text[4:] + text[0:4] + 'ay')
    elif text[0] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[1] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[2] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        print((text), 'translates to', text[3:] + text[0:3] + 'ay')
    elif text[0] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' and text[1] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        print((text),'translates to', text[2:] + text[0:2] + 'ay')
    elif text[0] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        print((text),'translates to', text[1:] + text[0:1] + 'ay')
    text = input('Type another word, or type 0 to quit: ')

