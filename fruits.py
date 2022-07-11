 # 10/31/18
# Nicholas Soluri
# Dr. Burhans CSC 111 Lab
# fruits.py


mylist = [ ['apple', 'banana', 'orange', 'mango', 'plum'], [.50, .34, .55, .65, .44], [2, 4, 6, 3, 7]]
index = 0
fruitlist = mylist[0]
pricelist = mylist[1]
quanlist = mylist[2]

import math
index = 0


while index < len(mylist[0]):
    print('Item:', '          ', mylist[0][index])
    print('Price:', '         ', '$', '%.2f' % (mylist[1][index]))
    print('Quantity:', '      ', mylist[2][index])
    print('Total:', '         ', '$', '%.2f' % (mylist[1][index] * mylist[2][index]))
    print()
    index +=1
