"""
Rock, Paper, Scissors (Extended Version)
"""
import random
print("WElcome To Rock Paper Scissors Game ")
cho=["Rock","paper","Scissors"]
win=0
com=0
for i in range(5):
    c=random.randrange(0,3)
    u=random.randrange(0,3)
    co=cho[c]
    us=cho[u]
    if us=="Rock" and co=="Rock":
        print("Its a draw !!!")
    elif us == "Rock" and co=="paper":
        print("Computer wins")
        com=com+1
    elif us=="Rock" and co == "Scissors":
        print("Computer wins ")
        com=com + 1
    elif us == "paper" and co == "paper":
        print("Its a draw !!!")
    elif us == "paper" and co == " Rock":
        print("Users wins ")
        win = win + 1
    elif us =="paper" and co == "Scissors":
        print("Computer wins !!!")
        com=com+1
    elif us == "Scissors" and co == "Scissors":
        print("Its a draw ")
    elif us == "Scissors" and co == "Rock":
        print("Computer wins !!!")
        com=com+1
    elif us == "Scissors" and co == "paper":
        print("computer wins !!!")
        com= com+1
    w=input("Enter continue next round !!!")
if com>win:
    print("Computer wins the Game ")
elif com<win:
    print("User wins the Game ")
