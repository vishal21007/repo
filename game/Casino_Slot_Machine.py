# Programming Project: Casino Slot Machine (User vs System), V1

import random

symbols = {1: 'Cherry', 2: 'Lemon', 3: 'Orange', 4: 'Star', 5: 'Diamond', 6: 'Seven', 7: 'Jackpot'}
sys_wallet = 1000
user_wallet = 1000

print('Welcome to CASINO SLOT MACHINE')
print('------------------------------')
print('User Balance   : ', sys_wallet)
print('System Balance : ', user_wallet)

while True:
    print('\n1. Single Spin Mode\n2. Multi-Round Mode (Best of 5)\n0. Exit')
    ch_user = int(input('Enter your choice: '))

    if ch_user == 1:
        print('\n--- SINGLE SPIN MODE ---\n')
        print('Your current balance   : ',user_wallet)
        print('System current balance : ',sys_wallet)

        user_bet = int(input('Enter your bet amount: '))

        # system betting logic !
        lower_limit = int(0.10*sys_wallet)
        upper_limit = int(0.25*sys_wallet)
        sys_bet = random.randint(lower_limit,upper_limit)
        print('System bets: ',sys_bet)
        
        print('\nSpinning slots...\n')

        user_deck = []                  # holding bet for user
        sys_deck = []                   # holding bet for system

        # adding bet to user list.
        for i in range(3):              
            bet_value = random.randint(1,7)
            user_deck.append(bet_value)     
        
        # adding bet to system list.
        for j in range(3):              
            bet_value = random.randint(1,7)
            sys_deck.append(bet_value)     
        
        print("User Slots   :  [ " + symbols[user_deck[0]] + " | " + symbols[user_deck[1]] + " | " + symbols[user_deck[2]] + " ]")
        print("System Slots   :  [ " + symbols[sys_deck[0]] + " | " + symbols[sys_deck[1]] + " | " + symbols[sys_deck[2]] + " ]")

        # winning condition

        