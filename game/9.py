"""
Write a program to create a game, roll a dice. every time game rolls a dice, user need to predict the number. If 
numbers entered by user is same as of dice then respond - number is
 correct else incorrect. total of 5 chances, if user gets 3 correct prediction, user wins the games else loses the game.
"""
win=0
import random
for i in range(5):
    num=random.randrange(7)
    nu=int(input("Enter your prediction between 1 -6 : "))
    if num==nu:
        win=win+1
        print("You guessed it correct ")
    else:
        print("You didnt guessed it correct ")
    if win==3:
        print("You won the game : ")
        break
    if i == 4 and win != 3 :
        print("you lose the game please tyr again ")
        break