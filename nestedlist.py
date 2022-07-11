# in-class nested lists
# multi dimesional 'arrays'
# we will look at square, rectangular, and ragged
# Nicholas Soluri 01/31/18
# Dr. Burhans CSC 111 Lab

# need to be able to index into a single location
# note: 2 indexes, one for top level list and one for inner level
# need to be able to print  row at a time
# need to nicely format values

# square 2-d list:
# [ [1,2,3], [4,5,6], [7,8,9] ]
# when printed as a table looks like this:
# 1 2 3
# 4 5 6
# 7 8 9
def getElement(row, col, mytable):
    
        return (mytable[row][col])

    









table3x3 = [ [1,2,3], [4,5,6], [7,8,9] ]
# unformatted prints a list of lists
print(table3x3)
print()
print()

# want to iterate over the elements in a rows


# print an item at a time, note: items are themselves
for row in table3x3:
    print(row)

numrows = len(table3x3)
numcols = len(table3x3[0])

for row in range(numrows):
    print('Row:', row)
    for col in range(numcols):
        print('Col:', col, table3x3[row][col], end=' ')
    print() 

print()
print()


# non-square rectangular 'array'
# looks like
# 0 1 2 3 4
# 5 6 7 8 9 
table2x5 = [ [0,1,2,3,4], [5,6,7,8,9] ]
for row in table2x5:
    print(row)

numrows = len(table2x5)
numcols = len(table2x5[0])

for row in range(numrows):
    print('Row:', row)
    for col in range(numcols):
        print('Col:', col, table2x5[row][col], end=' ')
    print() 

print()
print()
table = [ [0,1,2,3,4], [5,6,7,8,9] ]


numrows = len(table)
numcols = len(table[0])

index  = 0


while index < len(table[0]):
    newcol = table[0][index], table[1][index]
    print('column', index, newcol)
    index +=1

  
print()
print()








#ragged array -- array where rows can have different lenghts
# ex
# 1 2
# 3 4 5 6
# 7
# 8 9 10

raggedTable4rows = [ [1,2], [3,4,5,6], [7], [8,9,10] ]

numrows = len(raggedTable4rows)
numcols = len(raggedTable4rows[0])

for row in range(numrows):
    
    numcols = len(raggedTable4rows[row])
    print('Row:', row, 'has', numcols, 'columns.')
    for col in range(numcols):
        print('Col:', col, raggedTable4rows[row][col], end=' ')
    print() 

print()
print()

# Note: we can always use the above to print any type of array
# NOW:
# 1 : add code to print a column at a time -- one column per line
# ---- for rectangular list
# ex: table 3x3 would produce this
# 1 4 7
# 2 5 8
# 3 6 9

# 2 : write a function called getElement(row, col, mytable)
# ---- definition at the top of code
# 3 parameters a row number, column number, and a table
# returns the item in that row and column of the table
# test your function with these calls



table3x3 = [ [1,2,3], [4,5,6], [7,8,9] ]
table2x5 = [ [0,1,2,3,4], [5,6,7,8,9] ]


print(getElement(0, 2, table3x3))
print(getElement(1, 3, table2x5))




