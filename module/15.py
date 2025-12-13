""" Dice Roll

Write a code to roll dice in such a way that every time you get the same number.

Dice has 6 numbers (from 1 to 6). 
Roll dice in such a way that every time you must get the same output number. do this 5 times.
"""
import random
i=1
Flag = True
while i<=5:
    s=random.randrange(1,7)
    if Flag == True:
        s1 = s
        Flag=False
    if s==s1:
        print(s)
        i=i+1
    else:
        continue
