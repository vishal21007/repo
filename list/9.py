lst=[1,2,3,4,5,6,7,8,9]
l=len(lst)
mid=int(l/2)
for i in range(mid):
    lst[i,mid+1]=mid+1,lst[i]
print(lst)