# WAP to count the number of strings where the string lenght is 2 or more and the first and 
# last characters are same from a given list of strings.

lst = ['aba','xyz','121','bob','112'] # sample list
count = 0
for i in lst:
    if len(i) >= 2 and i[0]==i[-1]:
        print(i)
        count = count + 1
print('Total Count : ',count)


'''
count=0
count1=0
for i in range(len(lst)):
    if len(lst[i]) > 2 :
        count=count+1
    for j in lst[i]:
        print(lst[j])
print("There are",count,"string length more than 2 ")    
'''
