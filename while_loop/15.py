'''
Make a while loop menu
1. Add order value
2. Print order value
3. Exit
'''

lst=[]
while True:
    print("Press 1 : To add order value ")
    print("Press 2 : To print order value ")
    print("press 3 : To exit the program")
    ch=int(input("Enter your choise : "))
    if ch == 1:
        var=int(input("Enter your order valve :"))
        lst.append(var)
        print('')
    elif ch == 2:
        sum=0
        for i in lst:
            sum = sum + i
        print("Your order value is:",sum)
    elif ch == 3:
        break
    else : 
        print("Invalid inpot!")
