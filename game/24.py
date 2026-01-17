import random
print("===Tic-Tac-Toe-Game===")
while True:
    print("--Main - Menu--\n")
    print("1 : Play Single Round ")
    print("2 : Play Multi Round ")
    print("0 : To Exit ")
    ch=int(input("Enter your choice : "))
    if ch == 1:
        user_symbol=random.randint(0,1)  #Assining symbol to 
        if user_symbol==0:
            user_symbol="X"
            system_symbol="0"
        else:
            user_symbol="0"
            system_symbol="X"
        print("\nThe Game has assined you as :",user_symbol," and system as : ",system_symbol,"\nYou go first \n")
        print("Current board:")
        count=0
        for i in range(3):
            if i==0:
                print("position : ,end=)
            elif i==1:
                print("position : ",count,' ',end="| ")
            elif i==2:
                print("position : ",count,' ',end="| ")
            
            for j in range(3):
                if  j == 2:
                    continue
                else:
                    print(' '*4,end="| ")
                count=count+1
            print('\n---------------')