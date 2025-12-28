# High card game 

import random

dec={1:"2",2:"3",3:"4",4:"5",5:"6",6:"7",7:"8",8:"9",9:"10",10:'Jack',11:'Queen',12:'King',13:'Ace'}

def single_play(): # single round game
    print("Rules: Draw a card. Higher card wins!\nCard values: 2-10 < Jack < Queen < King < Ace")
    user=[]
    count=0
    while True:
        usr=random.randint(1,13)
        if dec[usr] not in user:
            count = count + 1
            print("Position : ",count," Crad ",dec[usr])
            user . append (dec[usr])
        if count==5:
            break
    pic=int(input("Enter the card no. you selected : "))
    com=random.randint(1,13)
    print("System's card : ",dec[com])
    print("User's card : ",user[pic-1])     
    print("Result : ")
    if user[pic-1]>dec[com]:
        print("User win's the game ") 
    elif user[pic-1]<dec[com]:
        print("Computer win's the game !!!!") 
    else:
        print("It's a draw !!")

#Menu 


print("***--- Welcome - To - High Card Wins ---***")
print("1. Play Single Rounds ")
print("2. Play Multiple Rounds with score Tracking ")

gm=int(input("Choose Game Mode (1 or 2) : "))
print("==============================\n           HIGH CARD WINS \n==============================")
if gm == 1:
    sin=single_play()
    print(sin)
elif gm == 2:
    b=0
    b1=0
    user=[]
    comp=[]
    print("---*** Multi Round Game (Best of 5) ***---")
    while True:

        usr=random.randint(1,13)
        com=random.randint(1,13)
        if dec[usr] not in user:
            user.append(dec[usr])  
            b1=b1+1
        if dec[com] not in comp:
            comp.append(dec[com]) 
            b=b+1     
        if b>=5 and b1>=5:
            break
    round=1
    
    u_=0
    c_=0
    draw=0
    while True:
        count=1
        print("Round : ",round)
        co=random.randint(1,5)
        s_card=comp[co-1]
        print("System has genarated its card \n")
        for i in user:
            print("Position : ",count," card ",i)
            count=count+1
        pic=int(input("Enter you'r selected card number : "))
        print("System's card : ",s_card)
        print("User's card : ",user[pic-1])
        if user[pic-1]>s_card:
            print("Result : User win's the game ")
            del (user[pic-1])
            u_=u_+1
            print("Score after Round ",round,":\nUser: ",u_, "| System: ",c_,"| Draws: ",draw,"\n---------------------------------")
            print("\n")
            round=round+1
        elif user[pic-1]<s_card:
            print("Result : Computer win's the game !!!!")
            c_=c_+1
            print("Score after Round ",round,":\nUser: ",u_, "| System: ",c_,"| Draws: ",draw,"\n---------------------------------")
            print("\n")
            round=round+1
            del (user[pic-1])
            del s_card
        else:
            print("Result : It's a draw !!")
            draw=draw+1
            print("Score after Round ",round,":\nUser: ",u_, "| System: ",c_,"| Draws: ",draw,"\n---------------------------------")
            print("\n")
            round=round+1
            del (user[pic-1])
            del s_card
        if round==6:
            break
print("Final Result ")
if u_>c_:
    print("User wins the game !!!")
elif u_<c_:
    print("System wins the game !!!")
else:
    print("The game ha been drawed !!!!!!!")
print("\n")
print("Final score : ")
print("User : ",u_)
print("System : ",c_)
print("Draw's : ",draw)