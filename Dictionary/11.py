"""1 train booking 
2 train info
3 food services 
4 seat avalibility 
"""
train={"t001":["Mumbai express",1400,"14hr",120],"t002":["bikaneer express",900,"10hr",90],"t003":["J and K express",1400,"17hr",85]}
while True:
    print("press 1 : Book seat ")
    print("press 2 : Train information ")
    print("press 3 : Food service ")
    print("press 4 : Check available seats ")
    print("press 0 : To Exit ")
    ch=int(input("Enter your choice : "))
    if ch == 1 :
        fair=0
        print("train_no. \t t_name \t \t t_fair \t t_duration \t seat_avilabe ")
        for keys , values in train.items():
            print(keys,"\t \t",values[0],"\t",values[1],"\t \t ",values[2],"\t \t ",values[3])
        t_id=input("Enter your selected train no. : ")
        for i in train[t_id]:
            if type(i)==int:
                t_no=int(input("Enter no. of seats : "))
                nm=input("Enter your name : ")
                num=int(input("Enter your contact number : "))
                print(" IRCTC SERVICE \n Train id",t_id,"\n Name :",nm,"\n Number of seats :",t_no,"\n Mobile number :",num,"\n Sum payed :",i*t_no)
                ye=input("do you want to EXIT yes/ no : ").lower()
                if ye=="yes":
                    break
        # stop loop from exiting, so user could read the information
        # ask user : Do you want to continue(y/n):  , if user enter y then continue the code

    elif ch ==2 :
        t=input("Enter your train id : ")
        if t in train:
            print("train_no. \t t_name \t \t t_fair \t t_duration \t seat_avilabe ")
            print(train[t])
        else : 
            print("Invalid train id !!!")
    elif ch ==3:
        t=input("Enter your train id : ")
        if t in train:
            print("Food isn't available at the moment ")
        else : 
            print("Invalid train id !!!")
    elif ch == 4:
        t=input("Enter your train id : ")
        if t in train:
            for keys , values in train.items():
                if t == keys:
                    print("Available seats in the train",t,"is : ",values[3])

        else : 
            print("Invalid train id !!!")
    elif ch == 0:
        break
    else:
        print("Invalid input !!!!")