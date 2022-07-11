from infiniteint3 import *

#  Note that you have to have the file infiniteint3.py in the same directory as this file.

n1 = InfiniteInt("81673")
n2 = InfiniteInt("3242")

n3 = n1.add(n2)
print(n3.mystring)

n1 = InfiniteInt("999")
n2 = InfiniteInt("1")

n3 = n1.add(n2)
print(n3.mystring)

num = input("Enter a long integer (no decimal points!) ")
n4 = InfiniteInt(num)
print(n4.commaize())

print(n4.toscientific())