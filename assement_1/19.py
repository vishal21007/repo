L= [11,34,56,23,67,78]
l=[]
for i in L:
    if i == 78:
        continue
    else:
        l.append(i)
print(l)
l.insert(4,89)
print(l)
l.sort()
print(l)
del l[::]
print(l)