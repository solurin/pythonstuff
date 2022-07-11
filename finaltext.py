##Nicholas Soluri
#CSC 111 Lab Dr. Burhans
#Lab 11 text.py

infile = open('raven.txt')
infile = infile.read()
##
##wordlist = list(infile)
##print(str(wordlist[8:]))
d = {}
for i in infile:
    d[i] = infile.count(i)
for k in sorted(d):
    print(k + ': ' + str(d[k]))

    
        
mylistoftuples = list(d.items())


mylistoftuples.sort( key = lambda x:x[1])



print('Ten least frequently occurring characters:', mylistoftuples[0:10])
print()
print('Ten most frequently occurring characters:', mylistoftuples[54:])


##mywords = (infile.split())
##
##d = {}
##for item in mywords:
##    d[item] = mywords.count(item)
##
##wordtuples = list(d.items())
##del wordtuples[575]
##del wordtuples[574]
##del wordtuples[573]
##del wordtuples[571]
##del wordtuples[570]
##del wordtuples[567]
##del wordtuples[564]
##del wordtuples[563]
##del wordtuples[559]
##del wordtuples[558]
##del wordtuples[551]
##del wordtuples[546]
##del wordtuples[545]
##
##wordtuples.sort(key = lambda x:x[1])
##
##print(wordtuples)
##print()
##print('The ten least occuring words are', wordtuples[0:10])
##print('The ten most occuring words are', wordtuples[553:])

##
# i is but in and no my i, a of the or
##575, 574, 573, 571, 570, 567, 564, 563, 559, 558, 551, 546 545, 

