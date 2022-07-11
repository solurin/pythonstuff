#Nicholas Soluri
#Lab Assignment 2a
#9/12/18


bin = input('Enter a binary number: ')
sum=0
exp = len(bin) - 1


for digit in bin:
    val = int(digit) * 2 ** exp
    sum = sum + val
    exp = exp - 1

print(sum)

