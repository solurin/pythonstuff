# Nicholas Soluri
# 9/19/18 Lab 4
# letters.py

intext = input('Type something: ')
#set counts for letter and nonletter to 0
countoflet = 0
countofnonlet = 0
for ch in intext:
    
    
#if---- its a letter add 1 to the count of letters
#else--- add 1 to the count of non letters
    
    
    if ch>= "A" and ch<= "Z" or ch>= 'a' and 'z':
        countoflet +=1
    else:
        countofnonlet +=1
        
print('There are', countoflet, 'letters in your input.')
print('There are', countofnonlet, 'nonletters in your input.')

# we will also determine the number of letters and non letters in the following
# excerpt


text = '''Stately, plump Buck Mulligan came from the stairhead, bearing a bowl of
lather on which a mirror and a razor lay crossed. A yellow dressinggown,
ungirdled, was sustained gently behind him on the mild morning air. He
held the bowl aloft and intoned:

—Introibo ad altare Dei.

Halted, he peered down the dark winding stairs and called out coarsely:

—Come up, Kinch! Come up, you fearful jesuit!

Solemnly he came forward and mounted the round gunrest. He faced about
and blessed gravely thrice the tower, the surrounding land and the
awaking mountains. Then, catching sight of Stephen Dedalus, he bent
towards him and made rapid crosses in the air, gurgling in his throat
and shaking his head. Stephen Dedalus, displeased and sleepy, leaned
his arms on the top of the staircase and looked coldly at the shaking
gurgling face that blessed him, equine in its length, and at the light
untonsured hair, grained and hued like pale oak.

Buck Mulligan peeped an instant under the mirror and then covered the
bowl smartly.

—Back to barracks! he said sternly.'''
countoflet2 = 0
countofnonlet2 = 0
for ch in text:
    if ch>= "A" and ch<= "Z" or ch>= 'a' and 'z':
        countoflet2 +=1
    else:
        countofnonlet2 +=1

print(text)
print('There are', countoflet2, 'letters in this excerpt.')
print('There are', countofnonlet2, 'nonletters in this excerpt.')



