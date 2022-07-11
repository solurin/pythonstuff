#Nicholas Soluri
#CSC 111 Dr. Burhans
#9/26/18
#scores.py---- using a loop to count score by 1
sum = 0
score = 0
count = 0
sumsc = 0
score = int(input('enter your score:'))

while score >= 0 :
    sum = sum + score
    count = count + 1
    score = int(input('Enter another score, or a negative number to quit:'))
           
avg = (sum / count)
print('the sum is', sum)
print('the avg of scores is', avg)



