# High card game V2
 
import random

dec={1:"2",2:"3",3:"4",4:"5",5:"6",6:"7",7:"8",8:"9",9:"9",11:'Jack',12:'Queen',13:'King',14:'Ace'}

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
#Multiple times play

def multiple_round():
    deck = {2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'JACK',12:'QUEEN',13:'KING',14:'ACE'}

    print("--- Multi Round Game (Best of 5) ---")
    user=0
    system=0
    draw=0
    for i in range(5):
        print("--- Round ",i+1 ," : ---")
        sis_deck=random.randint(2,14)
        print("\nSystem has drawn its card \n")
        print("User : Suffeling card for you -\nAvailable cards for you")
        user_deck=[]
        while True:
            value=random.randint(2,14) #generating random card for user
            if value not in user_deck:
                user_deck.append(value)
            if len(user_deck) == 5:
                break
        for i in range(5):
            print("Position : ",i+1," Crad ",deck[user_deck[i]])
        print(" ")
        ch=int(input("Enter the card you want to play (enter position) : "))
        print("System card : ",deck[sis_deck])
        print("User's card : ",deck[user_deck[ch-1]])
        print(" ")
        print("Result")
        print("Score after round ",i+1)
        
        if sis_deck<user_deck[ch-1]:
            print("user win's the round")
            user=user+1
        elif sis_deck>user_deck[ch-1]:
        
            system=system+1
            print("system win's the round")
        else:
        
            draw=draw+1
            print("The round is draw")
        print("User :",user," System :",system," Draw :",draw,"\n")
    print("--- Final Result ---")
    if system>user:
        print("System win's the Game ")
    elif system<user:
        print("User win's the Game")
    else:
        print("The Game has been drawed !!!!")
    print(" ")
    print("--- Final Score ---")
    print("User : ",user)
    print("System : ",system)
    print("Draw : ",draw)


        



    #Menu 


print("***--- Welcome - To - High Card Wins ---***")
while True:
    print("1. Play Single Rounds ")
    print("2. Play Multiple Rounds with score Tracking ")
    print("0 : To Exit")
    gm=int(input("Choose Game Mode (1 or 2) : "))
    print("==============================\n           HIGH CARD WINS \n==============================")
    if gm == 1:
        sin=single_play()
        print(sin)
    elif gm == 2:
        mul=multiple_round()
        print(mul)
    elif gm == 0:
        break
    else:
        print("invalid input")