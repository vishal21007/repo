#wapa menu drivent program to input your frinds name and store them in dict
#1 diplay dist 
# 2 add new nm , number 
# 3 modefy ph no. od friend 
# 4 delet entry 
# 5 search details 
# display sorted dict

dic={}
while True:
    
    print("press 1 : add new friend ")
    print("press 2 : display directory ")
    print("press 3 : to change details ")
    print("press 4 : to delet friend ")
    print("press 5 : search contact ")
    print("press 6 : sort the directory ")
    print("press 7 : to exit ")
    ch=int(input("Enter your choice : "))
    if ch == 2:
        print("Name \t Contact number ")
        for keys , values in dic.items():
            print(keys,"\t",values)
    elif ch == 1 :
        n=int(input("Enter no. of friends you want add : "))
        for i in range(n):
            nm=input("Enter name of your friend : ")
            no=int(input("Enter number of your friend : "))
            dic[nm]=no
    elif ch ==3 :
        nm1=input("Enter name you friend you want to edit : ")
        no1=int(input("Enter number : "))
        if nm1 in dic:
            dic[nm1]=no1
        else:
            print("Friend not in contact ")
    elif ch == 4:
        nm2=input("Enter name you friend you want to delet : ")
        if nm2 in dic:
            del dic[nm2]
        else:
            print("Friend not in contact ")
    elif ch == 5:
        nm3=input("Enter your friends name you search : ")
        if nm3 in dic:
            print(dic[nm3])
        else:
            print("Friend not in contact ")
    elif ch == 6:
        sorted(dic)
        print(dic)
    elif ch ==7 :
        break
    else:
        print("Invalid input")