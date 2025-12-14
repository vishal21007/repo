'''
Number Quest Function
'''

import random

lst = [ 11,22,33,44,55,66,77 ]
print("This is the list : ",lst,"You'll get 3 try to play the game ")

dic={}
win=[]
nm=input("Enter your name : ") # name of user

for i in range(3):
    gus=random.randrange(0,7)
    num=int(input("Enter your guess : "))
    if lst[gus]==num:
        win.append(1)
    else:
        win.append(0)
dic[nm]=win
print('Result : ',dic)