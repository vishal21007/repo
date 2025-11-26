"""guess the number:1-10"""
print("Welcome to the guess game ")
import random
s=random.randrange(1,10)
print("The number has been generated  ")
nu=int(input("Guess a number between 1 to 10 : "))
if s == nu:
    print("You guessed the right number ")
else:
    print("You guessed the wrong number !!!!!")