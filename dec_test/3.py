"""print even index vakues of lst"""
lst=[1,2,3,4,5,6,7,8,9,0,11,2,2,3,33,44,55,66]
for i in range(len(lst)):
    if i%2==0:
        print(lst[i],end=" ")