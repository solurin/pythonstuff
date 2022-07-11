#Nicholas Soluri
#Lab 4 9/19/19
#piglatin.py

text = input(str('Say something:'))



for ch in text[0]:
        if ch in 'aeiou' or ch in 'AEIOU':
            print(text + 'yay')
        if ch in 'bcdfghjklmnpqrstvwxz' or ch in 'BCDFGHJKLMNPQRSTVWXYZ':
            print((text[1:] + (text[0] + 'ay'))) 
            
