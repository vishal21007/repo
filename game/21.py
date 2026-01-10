import random
deck = {2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'JACK',12:'QUEEN',13:'KING',14:'ACE'}
system_deck=[]
while True:
    sis_card=random.randint(2,14)
    if sis_card not in system_deck:
        system_deck.append(sis_card)
    if len(system_deck) == 5:
        break
user_deck=[]
while True:
    usr_card=random.randint(2,14)
    if usr_card not in user_deck:
        user_deck.append(usr_card)
    if len(user_deck) == 5:
        break
win=0
lose=0
draw=0
for i in range(5):
    print("\n--- Round - ",i+1," ---\n")
    system=random.randint(0,len(system_deck))
    print("System has drawn it's card \n")
    for i in range(len(user_deck)):
        print("Card Position : ",i+1," card = ",deck[user_deck[i]])
    print(" ")
    ch=int(input("Enter your selected card position : "))
    print("\nSystem's card :",deck[system_deck[system-1]])
    print("User's card : ",deck[user_deck[ch-1]])
    if system_deck[system-1] > user_deck[ch-1]:
        print("System win's the round ")
        lose=lose+1
        print("Round Score \nUser : ",win,"| System : ",lose,"| Draw : ",draw)
    elif system_deck[system-1] < user_deck[ch-1]:
        print("User wins the round ")
        win=win+1
        print("Round Score \nUser : ",win,"| System : ",lose,"| Draw : ",draw)
    else:
        print("The round has been drawed !!!")
        draw=draw+1
        print("Round Score \nUser : ",win,"| System : ",lose,"| Draw : ",draw)
    
    user_deck.remove(user_deck[ch-1])
    system_deck.remove(system_deck[system-1])
print("\n--- Final - Result ---")
print("User :",win)
print("System :",lose)
print("Draw :",draw)
if win>lose:
    print("User win's the Game ")
elif win<lose:
    print("System win's the Game ")
else:
    print("The Game has been Drawed !!!")