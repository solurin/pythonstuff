# list.py
# Nicholas Soluri
# 10/3/18 CSC 111 Dr. Burhans

list1 = [1,3,5]
list2 = [2,4,6]
list3 = []
sumlist = []

index = -1
while index <= len(list2):
    index +=1
    list3 = sumlist.append(list1[index] +list2[index])
    print(sumlist)



