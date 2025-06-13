'''
wap that reads 2 num and performs 1 on arthematic operation post user input
'''
num1=float(input("Enter a number : "))
num2=float(input("Enter a number : "))
print("press 1: for addition ")
print("press 2: for subraction ")
print("press 3: for multiplaction ")
print("press 4: for devision ")
ch=int(input("Enter your choise : "))
if ch == 1:
    pr=num1+num2
    print(pr)
elif ch == 2:
    if num1<num2:
        pr=num2-num1
        print(pr)
    elif num1>num2:
        pr=num1-num2
        print(pr)
elif ch == 3:
    pr=num1*num2 
    print(pr)
elif ch == 4:
    if num1<num2:
        pr=num2/num1
        print(pr)
    elif num1>num2:
        print("This devision can not be done !")
else:
    print("Invalid input !!!")