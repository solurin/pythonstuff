#Nicholas Soluri
#Lab 4 9/19/19
#vowels.py

countv = 0
countc = 0
countnonlet = -2

text = input('Say something:')
for ch in text:
        if ch in 'aeiou' or ch in 'AEIOU':
            countv +=1
        if ch in 'bcdfghjklmnpqrstvwxz' or ch in 'BCDFGHJKLMNPQRSTVWXYZ':
            countc +=1
        else:
            countnonlet = countnonlet + 1
            
print('There are', countv, 'vowels in your input')
print('There are', countc, 'consonants in your input')
print('There are', countnonlet, 'nonletters in your input')
