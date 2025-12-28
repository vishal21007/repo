# High Card Wins

import random

dec={1:"2",2:"3",3:"4",4:"5",5:"6",6:"7",7:"8",8:"9",9:"10",10:'Jack',11:'Queen',12:'King',13:'Ace'}

print("***--- Welcome - To - High Card Wins ---***")
print("1. Play Single Rounds ")
print("2. Play Multiple Rounds with score Tracking ")

gm=int(input("Choose Game Mode (1 or 2) : "))
print("==============================\n           HIGH CARD WINS \n==============================")

if gm == 1:
    print("Rules: Draw a card. Higher card wins!\nCard values: 2-10 < Jack < Queen < King < Ace")
    user=[]
    comp=[]
    count=0
    for i in range(8):
        us = random.randint(1,13)
        co = random.randint(1,13)
        if dec[us] not in user : 
            count = count + 1
            print('Position : ',count, end=' ')
            print('Card : ',dec[us])
            user.append(dec[us])
        if dec[co] not in comp :            
            comp.append(dec[co])
        
    pic = int(input('Enter the card position to play : '))
    c=random.randint(1,5)
    print("System card :",comp[c-1])
    print("Your card : ",user[pic-1])
    print("Result :")
    if user[pic-1] > comp[c-1]:
        print("User wins the game ")
    elif user[pic-1] == comp[c-1]:
        print("Its a draw !!!")
    else:
        print("Computer wins the game ")