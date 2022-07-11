#Nicholas Soluri
#Lab 4 B
#CSC 111 Dr. Burhans
#9/19/18

f = open('ulysses.txt', encoding = 'utf-8')
lines = f.readlines()

countqm = 0
countthe = 0
countz = 0
countq = 0
for line in lines:
    if "?" in line:
        countqm +=1
    if "the" in line:
        countthe +=1
    if "z" in line:
        countz +=1
    if "q" in line:
        countq +=1
        
lenlines = len(lines)
print('There are', countqm, 'question marks,', countthe, 'thes', countz, 'zs')
print('and', countq, 'qs, and the text is', lenlines, 'lines long.')







        
