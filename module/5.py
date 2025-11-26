"""wap which adds random even number in a list that falls in between highest and lowest number"""
hi=int(input("Enter the highest limit : "))
lo=int(input("Enter the lowest limit : "))
lst=[]
while True:
    import random
    s=random.randrange(lo,hi+1)
    if s%2==0:
        lst.append(s)
    else:
        continue
    if len(lst)==5:
        break
print(lst)