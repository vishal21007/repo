"""casino game """
import random

#Main program 

print("Welcome to Cashino Slot Game")
print("-----------------------------\n")
user_balance=1000
system_balance=1000
print("User Balance : ",user_balance)
print("System Balance : ",system_balance)
print("1. Single Spin Mode")
print("2. Multi-Round Mode (Best of 5)")
print("0. Exit")
game=int(input("Choose your Game mode "))
if game == 1:
    symbols = {1: 'Cherry', 2: 'Lemon', 3: 'Orange', 4: 'Star', 5: 'Diamond', 6: 'Seven', 7: 'Jackpot'}
    print("Your current balace :",user_balance)
    print("Sysem current balance :",system_balance,"\n")
    while True:
        user_bet=int(input("Enter your bet amount (min:100 - max:1000) : "))
        if user_bet<100 or user_bet > 1000:
            continue
        else:
            break
    system_bet=random.randint(100,250)
    print("system bet : ",system_bet)
    system=[]
    user=[]
    for i in range(3):
        system_symbol=random.randint(1,7)
        user_symbol=random.randint(1,7)
        system.append(system_symbol)
        user.append(user_symbol)
    print("\nSuffeling Slots !!! \n")
    print("User slots : [",symbols[user[0]]," | ",symbols[user[1]]," | ",symbols[user[2]]," ]")
    print("System slots : [",symbols[system[0]]," | ",symbols[system[1]]," | ",symbols[system[2]]," ]")
    if user[0]==user[1]==user[2]:
        print("User wins the bet into 10X")
        user_balance=user_balance+user_bet*10
    elif user[0]==user[1]==user[2]==6 or user[0]==user[1]==user[2]==7:
        print("User hits the jackpot and wins bet into 50X")
        user_balance=user_balance+user_bet*50
    elif user[0]==user[1] or user[1]==user[2] or user[0]==user[2]:
        print("user wins bet into 3X")
        user_balance=user_balance+user_bet*3
    else:
        print("No match\nUser loses the bet !!!")
        user_balance=user_balance-user_bet
    if system[0]==system[1]==system[2]:
        print("System wins the bet into 10X")
        system_balance=system_balance+system_bet*10
    elif system[0]==system[1]==system[2]==6 or system[0]==system[1]==system[2]==7:
        print("System hits the jackpot and wins bet into 50X")
        system_balance=system_balance+system_bet*50
    elif system[0]==system[1] or system[1]==system[2] or system[0]==system[2]:
        print("System wins bet into 3X")
        system_balance=system_balance+system_bet*3
    else:
        print("System loses the bet !!!\nNo match")
        system_balance=system_balance-system_bet 
    print("\nUpdated user balance\n")
    print("Your current balace :",user_balance)
    print("Sysem current balance :",system_balance)
elif game==2:
    symbols = {1: 'Cherry', 2: 'Lemon', 3: 'Orange', 4: 'Star', 5: 'Diamond', 6: 'Seven', 7: 'Jackpot'}
    print("--- MULTI-ROUND MODE (BEST OF 5) ---\n")
    print("Your current balace :",user_balance)
    print("Sysem current balance :",system_balance,"\n")
    win=0
    lose=0
    draw=0
    for i in range(5):
        print("\n---Round - ",i+1,"---\n")
        print("Your current balace :",user_balance)
        print("Sysem current balance :",system_balance,"\n")
        while True:
            user_bet=int(input("Enter your bet amount (min:100 - max:1000) : "))
            if user_bet<100 or user_bet > 1000:
                print("Please enter your a valid Bet")
                continue
            else:
                break
        system_bet=random.randint(100,250)
        print("system bet : ",system_bet)
        user_balance=user_balance-user_bet
        system_balance=system_balance-system_bet
        system=[]
        user=[]
        for i in range(3):
            
            system_symbol=random.randint(1,7)
            user_symbol=random.randint(1,7)
            system.append(system_symbol)
            user.append(user_symbol)
        print("\nSuffeling Slots !!! \n")
        print("User slots : [",symbols[user[0]]," | ",symbols[user[1]]," | ",symbols[user[2]]," ]")
        print("System slots : [",symbols[system[0]]," | ",symbols[system[1]]," | ",symbols[system[2]]," ]")
    
        if user==system:
            print("The round has been drawed 2!!!")
            draw=draw+1
        else:
            if user[0]==user[1]==user[2] and user.sort() != system.sort():
                print("User wins the round \nwins bet into 10X\nAmount won =",user_bet*10)
                user_balance=user_balance+user_bet*10
        #    system_balance=system_balance-system_bet
                win=win+1
            elif   system[0]==system[1]==system[2] and user.sort() != system.sort():
                print("System wins the round \nwins bet into 10X\nAmount won =",system_bet*10)
       #      us er_balance=user_balance-user_bet
                system_balance=system_balance+system_bet*10
                lose=lose+1
            elif user[0]!=user[1]!=user[2] and system[0]==system[1]==system[2]:
                print("System wins the round \nwins bet into 10X\nAmount won =",system_bet*10)
      #      user_balance=user_balance-user_bet
                system_balance=system_balance+system_bet*10
                lose=lose+1
            elif system[0]!=system[1]!=system[2] and user[0]==user[1]==user[2]:
                print("User wins the round \nwins bet into 10X\nAmount won =",user_bet*10)
                user_balance=user_balance+user_bet*10
     #       system_balance=system_balance-system_bet
                win=win+1
            elif (user[0] == user[1] or user[1] == user[2] or user[0] == user[2]) and system[0]!=system[1]!=system[2]:
                print("User wins the round \nwins bet into 3X\nAmount won =",user_bet*3)
                user_balance=user_balance+user_bet*3
    #        system_balance=system_balance-system_bet
                win=win+1
            elif (system[0] == system[1] or system[1] == system[2] or system[0] == system[2]) and user[0]!=user[1]!=user[2]:
                print("System wins the round \nwins bet into 3X\nAmount won",system_bet*3)
   #          user_balance=user_balance-user_bet
                system_balance=system_balance+system_bet*3
                lose=lose+1
            elif   user[0]!=user[1]!=user[2] and  system[1]!=system[2]!=system[0]:
                print("The round has been losed by both System and User!!!")
 #       user_balance=user_balance-user_bet
#        system_balance=system_balance-system_bet        #
            elif  (user[0]==user[1]==user[2]==6 or user[0]==user[1]==user[2]==7) and system[0]==system[1]==system[2]:
                print("User wins the jackpot \nBet into 50X \nAmount won = :",user_bet*50)
                user_balance=user_balance+user_bet*50
                system_balance=system_balance+system_bet*10
            elif (user[0]==user[1]==user[2]==6 or user[0]==user[1]==user[2]==7) and (system[0]!=system[1]!=system[2]):
                print("User wins the jackpot \nBet into 50X \nAmount won = :",user_bet*50)
                user_balance=user_balance+user_bet*50
  #          system_balance=system_balance-system_bet
            elif (user[0]==user[1]==user[2]==6 or user[0]==user[1]==user[2]==7) and (system[0] == system[1] or system[1] == system[2] or system[0] == system[2]):
                print("User wins the jackpot \nBet into 50X \nAmount won = :",user_bet*50)
                user_balance=user_balance+user_bet*50
                system_balance=system_balance+system_bet*3
            elif (system[0]==system[1]==system[2]==6 or system[0]==system[1]==system[2]==7) and user[0]==user[1]==user[2]:
                print("Sysrem wins the jackpot \nBet into 50X \nAmount won = :",system_bet*50)
                system_balance=system_balance+system_bet*50
                user_balance=user_balance+user_bet*10
            elif (system[0]==system[1]==system[2]==6 or system[0]==system[1]==system[2]==7) and  user[0]!=user[1]!=user[2]:
                print("Sysrem wins the jackpot \nBet into 50X \nAmount won = :",system_bet*50)
                system_balance=system_balance+system_bet*50
 #           user_balance=user_balance-user_bet
            elif (system[0]==system[1]==system[2]==6 or system[0]==system[1]==system[2]==7) and (user[0] == user[1] or user[1] == user[2] or user[0] == user[2]):
                print("Sysrem wins the jackpot \nBet into 50X \nAmount won = :",system_bet*50)
                system_balance=system_balance+system_bet*50
                user_balance=user_balance+user_bet*3
            else:
                print("The round has been drawed 1!!!")
                draw=draw+1
    print("--- FINAL RESULT ---\n")
    print("Rounds won by user : ",win)
    print("Rounds won by system : ",lose)
    print("Rounds drawes : ",draw)
    print("\nFinal wallet balance\n")
    print("Your current balace :",user_balance)
    print("Sysem current balance :",system_balance)