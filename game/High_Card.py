# Program 7 : High Card Wins (Mini Project)

import random

deck = {2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'Jack', 12:'Queen', 13:'King', 14:'Ace'}

def single_round():
    deck = {2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'Jack', 12:'Queen', 13:'King', 14:'Ace'}
    print('\n--- Single Round Game ---')
    sys_deck = random.randint(2,14)     # randomly selecting card for system
    print('\nSystem has drawn its card.\n')
    print('User : Shuffling 5 Cards - ')
    user_deck_list = []      # list to store 5 cards for user

    while True:         # creating deck of 5 cards for user
        user_deck = random.randint(2,14)
        if user_deck not in user_deck_list:
            user_deck_list.append(user_deck)
        if len(user_deck_list) == 5:
            break
    
    print('Available cards for you : ')
    for i in range(5):      # printing card for user
        print('Card Position : ',i+1, ' Card : ', deck[user_deck_list[i]])
    print(' ')
    ch = int(input('Enter the card you want to play (enter position) : '))

    print('System card : ', deck[sys_deck])     # printing system selecting value
    print('Your card : ', deck[user_deck_list[ch-1]])
    print('\nResult : ')

    if sys_deck == user_deck_list[ch-1]:
        print('This is a draw !')
    elif sys_deck < user_deck_list[ch-1]:
        print('Congratulations! You win this round.')
    elif sys_deck > user_deck_list[ch-1]:
        print('System win this round.!')

def multi_round():
    deck = {2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'Jack', 12:'Queen', 13:'King', 14:'Ace'}
    print('\n--- Multi Round Game (Best of 5) ---')
    
    # system card deck : creating 5 card deck
    system_deck_list = []       # list to store 5 cards for system
    while True:                 # creating deck of 5 cards for system
        system_deck = random.randint(2,14)
        if system_deck not in system_deck_list:     # adding unique values only
            system_deck_list.append(system_deck)
        if len(system_deck_list) == 5:
            break
    
    # user card deck : creating 5 card deck
    user_deck_list = []         # list to hold 5 card
    while True:
        user_deck = random.randint(2,14)
        if user_deck not in user_deck_list:         # adding unique values in list
            user_deck_list.append(user_deck)
        if len(user_deck_list)==5:
            break
    
    for i in range(1,6):        # playing the game !
        print('--- Round ',i,': ---')
        sys_deck = random.randrange(0,len(system_deck_list))     # randomly selecting card from list - system_deck_list
        print('\nSystem has drawn its card.\n')
        
        print('User : Shuffling Cards - ')
        print('Available cards for you : ')
        for i in range(5):      # printing card for user
            print('Card Position : ',i+1, ' Card : ', deck[user_deck_list[i]])
        print(' ')
        ch = int(input('Enter the card you want to play (enter position) : '))
        print('\nSystem card : ', deck[user_deck_list[sys_deck]])     # printing system selecting value
        print('Your card : ', deck[user_deck_list[ch-1]])
        print('\nResult : ')

        # --- Scoring the wins/lose/draw ---
        score = {syst : 0, user : 0,draw:0}           # dictionary to hold the values
        if sys_deck == user_deck_list[ch-1]:
            print('Result: This is a draw !')
            score['draw'] = score['draw'] + 1
        elif sys_deck < user_deck_list[ch-1]:
            print('Result: Congratulations! You win this round.')
            score['user'] = score['user'] + 1
        elif sys_deck > user_deck_list[ch-1]:
            print('Result: System win this round.!')
            score['syst'] = score['syst'] + 1
        
        print('Score after Round',i ,':')
        print('User:', score['user'] ,' | System: ', score['syst'],'| Draws: ',score['draw'])
        del system_deck_list[sys_deck]
        del user_deck_list[user_deck]
    
    print('Final Result:')
    if score['user'] > score['syst']:
        print('User Wins the Game!')
    elif score['syst'] > score['user']:
        print('System Wins the Game!')
    else:
        print("The game ended in a overall Tie !")

    print('Final Score:')
    print('User : ', score['user'])
    print('System : ', score['syst'])
    print('Draw : ', score['draw'])

# Main Program Starts Here !
while True:
    print('Choose Game Mode:')
    print('1. Single Round Game')
    print('2. Multi Round Game (Best of 5)')
    print('0 : Exit')
    ch = int(input('Enter your choice : '))

    if ch == 1:
        single_round()
    elif ch == 2:
        multi_round()
    elif ch == 0 : 
        break
    else:
        print('Invalid Choice !')