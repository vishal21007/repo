"""print lst value in reverse with gap of 2"""
lst=[1,1,2,3,4,5,6,6,5,4,32,2,3,]
print(lst[::-2])
for i in range(1,len(lst)+1):
    if i%2==0:
        print(lst[len(lst)-i],end=" ")

