#Nick Soluri
#CSC 111 Dr. Burhans
#Final Image Lab 11/28/18
import math
infile = input('which file would you like to input?')

outfile = input('what is the name of the output file?')


inf = open(infile)
outf = open(outfile)

lines = inf.readlines()
outlines = outf.readlines()



def negate(text):
    for num in text:
        newnum = abs(num - 255)
        
    
