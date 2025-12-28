# rock paper scissors

import random

print("***** Welcome to Game : ******")
print("--- Rock, Paper, Scissors: Best of 5 ---")

lst=["rock", "paper", "scissors"]
co=0 # computer score
us=0 # user score
i=1 # user rounds

while True:
    print("--- Round", i ,"---")
    c=random.randrange(0,3)
    user=input("User : Enter your choice (rock, paper, or scissors) : ").lower()
    c1=lst[c]
    print("Computer choice : ",c1)
    if user =="rock" or user == "paper" or user == "scissors":
        if (user =="rock" and c1 == "scissors") or (user =="paper" and c1=="rock") or (user=="scissors" and c1=="rock"):
            print("User wins !!!")
            us=us+1
            i=i+1
            print("Scoreboard -> User:",us,"  | Computer: ",co)
        elif user == c1:
            print("It's a tie !!!")
            print("Scoreboard -> User: 0 | Computer: 0")
            i=i+1
        else :
            print("Computer wins !!! ")
            co=co+1
            print("Scoreboard -> User:",us,"  | Computer: ",co)
            i=i+1
    else:
        print("Invalid input! Please try again.")
        i=i+0
    if i ==6:
        break
    else:
        continue
print("-*-*-*GAME OVER*-*-*-")
if co>us:
    print("Computer wins the Game by : ",co-us)
elif co<us:
    print("User wins the Game by : ",us-co)
else:
    print("The Game has been drawed \nUser = ",us,"Computer = ",co)

    