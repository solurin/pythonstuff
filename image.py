#Nick Soluri
#CSC 111 Dr. Burhans
#Final Image Lab 11/28/18
import math


def negate(lines, outf):
    '''
        negate colors in the image by taking the absolute value of the
        initial value minus 255
    '''
    for i in range(3, len(lines)):
        line = lines[i].split()
        for j in range(len(line)):
            outf.write(str(abs(int(line[j])- 255)) + '\n')

def grayscale(lines, outf):
    '''
        turn the photograyscale by taking the average value of
        the 3 values of each RGB and replace the initial values
        with the average
    '''
    for i in range(3, len(lines)):
        line = lines[i].split()
        for j in range(0, len(line), 3):
            sums = int(line[j]) + int(line[j + 1]) + int(line[j + 2])
            average = sums // 3
            line[j] = average
            line[j + 1] = average
            line[j + 2] = average
            outf.write(str(line[j]) + '\n' + str(line[j + 1]) + '\n' + str(line[j + 2]) + '\n')

def highcontrast(lines, outf):
    '''
        make the image high contrast by making all values greater than 127 into
        255 and all other values 0

    '''
    for i in range(3, len(lines)):
        line = lines[i].split()
        for j in range(len(line)):
            if int(line[j]) > 127:
                line[j] = 255
                outf.write(str(line[j]) + '\n')
            else:
                line[j] = 0
                outf.write(str(line[j]) + '\n')


def removered(lines, outf):
    '''
        remove red form images by turning the first values of each RGB
        (the red value) into 0
    '''
    for i in range(3,len(lines)):
    
        line = lines[i].split()
   
        for j in range(len(line)):
            if j % 3 == 0:
                outf.write('0\n')
                
            else:
                outf.write(line[j]+ '\n')

def removegreen(lines, outf):
    '''
        remove red form images by turning the second values of each RGB
        (the green value) into 0
    '''
    for i in range(3,len(lines)):
    
        line = lines[i].split()
   
        for j in range(len(line)):
            if j % 3 == 1:
                outf.write('0\n')
                
            else:
                outf.write(line[j]+ '\n')


def removeblue(lines, outf):
    '''
        remove red form images by turning the third values of each RGB
        (the blue value) into 0
    '''
    for i in range(3,len(lines)):
    
        line = lines[i].split()
   
        for j in range(len(line)):
            if j % 3 == 2:
                outf.write('0\n')
                
            else:
                outf.write(line[j]+ '\n')

infile = input('which file would you like to input?')

outfile = input('what is the name of the output file?')
            
inf = open(infile)
outf = open(outfile, 'w')



lines = inf.readlines()
for i in range(3):
    outf.write(lines[i])

print('negate, grayscale, highcontrast, removered, removegreen, removeblue')

selection = input('what would you like to do to the image?')





if selection == 'negate':
    negate(lines, outf)
elif selection == 'grayscale':
    grayscales(lines, outf)
elif selection == 'highcontrast':
    highcontrast(lines, outf)
elif selection == 'removered':
    removered(lines, outf)
elif selection == 'removegreen':
    removegreen(lines, outf)
elif selection == 'removeblue':
    removeblue(lines, outf)


inf.close()
outf.close()
