#remove duplicate values from the list 
lst=[1,1,1,2,2,3,3,3,4,4,4,55,6,7,7,8,8,8,]
print(lst)
lst1=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)