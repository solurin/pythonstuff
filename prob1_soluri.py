###Nick Soluri
# CSC 111 Dr. Burhans
# lab exam practice

def average(name):
        newscorelist.append(student_scores[avgchoice])
        index = 0
        count = 0
        sum1 = 0
        while index < len(newscorelist[0]):
            sum1 = sum1 + newscorelist[0][index]
            count +=1
            index +=1
        averagescore = (sum1 / count)
        print('the average score for', avgchoice, 'is', averagescore)
        return '\n'






student_scores = {}

inval = input('what would you like to do?: add, view, avg, stop ')
while inval != 'stop':
    if inval == 'add':
        scorelist = []
        name = input('enter the name of a student: ')
        index = 0
        while index < 4:
            
            tscore = int(input('enter a test score value for this student: '))
            
            scorelist.append(tscore)
            index +=1
        student_scores[name] = scorelist
        inval = input('what would you like to do?: add, view, avg, quit ')
    elif inval == 'view':
        namechoice = input('which student\'s scores would you like to see?: ')
        print(student_scores[namechoice])
        inval = input('what would you like to do?: add, view, avg, quit ')
    elif inval == 'avg':
        newscorelist = []
        avgchoice = input('which student\'s scores would you like to find the average of?: ')
        print(average(avgchoice))        












