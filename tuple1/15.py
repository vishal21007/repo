"""
Computer v/s user : Roll a dice !
"""
import random

print(' ****  Welcome to game : Roll a Dice  ****')

dic={"user":"empty","compuer":"empty"}
com=[]
usr=[]

for i in range(5):
    ch=input("Do you want to roll once more :")
    c=random.randrange(1,7)
    u=random.randrange(1,7)

    if c>u:
        com.append(1)
    else:
        com.append(0)
    if c<u:
        usr.append(1)
    else:
        usr.append(0)
    if c==u:
        com.append(0)
        usr.append(0)
    print("---------------")
    print("***Round - ",i+1,"***")
    print("Computer got **",c,"** as product after rolling ")
    print("User got **",u,"** as product after rolling ")
    if c>u:
        print("Computer wins the round")
    elif c<u:
        print("User wins the round ")
    else:
        print("Both computer and user got same score")

dic["compuer"]=com
dic["user"]=usr
cu=sum(com)
us=sum(usr)
print("*** Game - Ends ***")
if cu>us:
    print("Computer wins the Game ")
elif cu<us:
    print("USer wins the Game")
else:
    print("Both Computer and User got same score \nGame is a Draw")