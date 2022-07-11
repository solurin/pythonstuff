###Nick Soluri
##

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
##        newscorelist.append(student_scores[avgchoice])
##        index = 0
##        count = 0
##        sum1 = 0
##        while index < len(newscorelist[0]):
##            sum1 = sum1 + newscorelist[0][index]
##            count +=1
##            index +=1
##        averagescore = (sum1 / count)
##        print('the average score for', avgchoice, 'is', averagescore)
##        inval = input('what would you like to do?: add, view, avg, quit ')   
##










##student_scores = {}
##
##name = input('enter the name of a student: ')
##ts1 = 0
##scorelist1 = []
##index = 0
##
##while index < 4:
##    ts1 = int(input('enter a test score value for this student: '))
##    scorelist1.append(ts1)
##    index +=1
##
##student_scores[name] = scorelist1
##
##
##
##name2 = input('enter the name of a student: ')
##ts2 = 0
##scorelist2 = []
##index = 0
##
##while index < 4:
##    ts2 = int(input('enter a test score value for this student: '))
##    scorelist2.append(ts2)
##    index +=1
##
##student_scores[name2] = scorelist2
##
##
##
##name3 = input('enter the name of a student: ')
##ts3 = 0
##scorelist3 = []
##index = 0
##
##while index < 4:
##    ts3 = int(input('enter a test score value for this student: '))
##    scorelist3.append(ts3)
##    index +=1
##
##student_scores[name3] = scorelist3
##
##
##
##name4 = input('enter the name of a student: ')
##ts4 = 0
##scorelist4 = []
##index = 0
##
##while index < 4:
##    ts4 = int(input('enter a test score value for this student: '))
##    scorelist4.append(ts4)
##    index +=1
##
##student_scores[name4] = scorelist4
##
##
##print(student_scores)
##
##
##
##studentchoice = input('choose a student: ')
##
##
##
##













##student_scores[name].append(int(input('enter a set of 4 scores for this student')))
##student_scores[name].append(int(input('enter a set of 4 scores for this student')))
##student_scores[name].append(int(input('enter a set of 4 scores for this student')))
##student_scores[name].append(int(input('enter a set of 4 scores for this student')))
##
##
##
##
##print(student_scores)
