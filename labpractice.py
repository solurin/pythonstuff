#nick soluri
#lab practice


##
##pets = {}
##petname = ''
##petspecies = ''
##
##petname = input('what is the name of your pet? Type 000 to quit: ')
##
##while petname != '000':
##    
##    petspecies = input('what kind of animal is it?: ')
##    pets[petname] = petspecies
##    petname = input('what is the name of your pet? Type 000 to quit: ')
##    


# polling friends

##friends = {}
##
##name1 = input('what is your name?: ')
##resp1 = input('are you tired?: ')
##name2 = input('what is your name?: ')
##resp2 = input('are you tired?: ')
##name3 = input('what is your name?: ')
##resp3 = input('are you tired?: ')
##friends[name1] = resp1
##friends[name2] = resp2
##friends[name3] = resp3
##print(friends)
##
##name = ''
##longest = ''
##for key in friends:
##    if len(friends[key]) > len(longest):
##        name = key
##        longest = friends[key]
##
##print('the longest response was from', name,':', longest)
##
##
##
##

# sum and average of a list of 20 numbers
##
##index = 0
##list1 = []
##
##
##while index < 20:
##    num = int(input('give me an integer: '))
##    list1.append(num)
##    index +=1
##              
##
##index = 0
##sum1 = 0
##while index < len(list1):
##    sum1 = sum1 + list1[index]
##    index +=1
##print('the sum of these numbers is', sum1)
##print('the average of these numbers is', (sum1/20)) 
##
##

### remove vowels of an input


##
##sent = input('type a sentence: ' )
##
##def removeVowels(sentence):
##    index = 0
##    newsent = ''
##    vowels = 'aeiouAEIOU'
##    while index < len(sentence):
##        if sentence[index] in vowels:
##            index +=1
##        elif sentence[index] not in vowels:
##            newsent = newsent + sentence[index]
##            index +=1
##
##    return newsent
##
##
##print(sent, 'without vowels is:', removeVowels(sent))
##            
##
##
































