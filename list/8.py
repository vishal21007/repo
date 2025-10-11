lst=[-1,23,-2,24,-22,45,-56]
lst1=[]
for i in lst:
    if i>0:
        lst1.append(i)
for j in lst:
    if j<0:
        lst1.append(j)
print(lst1)