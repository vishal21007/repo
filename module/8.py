"""Pick a Random Element from a List, also share there position a = [1, 2, 3, 4, 5, 6]"""
a = [1, 2, 3, 4, 5, 6]
import random
s=random.randrange(0,6)
print(a[s],"position is",a.index(a[s]))

""" Generate Random Negative Integers in a Range (-1 to -20)"""

s1=random.randrange(1,21)
print("-",s)

"""Write a code to generate 2 digit number using random()."""

s2=random.random()
print(int(s2*100))

"""Write a code to generate and add 5 even random numbers in a list, and sort values in the list.
"""
lst=[]
while True:
    import random
    s3=random.randrange(10,100)
    if s3%2==0:
        lst.append(s3)
    else:
        continue
    if len(lst)==5:
        break
lst.sort()
print(lst)