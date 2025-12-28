# Two-Player Dice Guessing Game

import random
dic={}
for i in range(2):
    nm=input("Enter your name : ")
    value = random.randint(0,2)
    win=0
    for j in range(5):
        num=random.randrange(1,7)
        gus=int(input("Enter your guess : "))
        if gus==num:
            win=win+1
        else:
            continue
    dic[nm]=win+value
name = list(dic.keys())
lst=list(dic.values())
if lst[0]>lst[1]:
    print('Winner is : ',name[0])
elif lst[0]<lst[1]:
    print('Winner is : ',name[1])
else:
    print("You both have scored same ")