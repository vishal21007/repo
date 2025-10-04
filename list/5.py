lst=[10,51,2,18,4,31,13,5,23,64,29]
E=[]
O=[]
for i in lst:
    if i%2==0:
        E.append(i)
    else:
        O.append(i)
print(E)
print(O)