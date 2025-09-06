# Remove duplicate elements while preserving order
tp=(1,2,2,4,4,5,43,4,5,3,2,2,4,3,2,)
lst = []
for i in tp:
    if i not in lst:
        lst.append(i)
tup = tuple(lst)
print(tup)