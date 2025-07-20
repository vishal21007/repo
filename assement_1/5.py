def add():
    a=int(input("Enter the 1st number :"))
    b=int(input("Enter the 2nd number :"))
    add=a+b
    print("The sum of",a,"and",b,"is",add)
def sub():
    a=int(input("Enter the 1st number :"))
    b=int(input("Enter the 2nd number :"))
    if a>b:
        sub=a-b
        print("the subtraction of",a,"from",b,"is",sub)
    elif a<b:
        sum=b-a
        print("the subtraction of",b,"from",a,"is",sub)
    else:
        print("Both the numbers are same",a,b)
def mult():
    a=int(input("Enter the 1st number :"))
    b=int(input("Enter the 2nd number :"))
    mult=a*b
    print("Multiplication of",a,"X",b,"is",mult)
def devi():
    a=int(input("Enter the divisor number :"))
    b=int(input("Enter the devidend number :"))
    devi=a/b
    print("The devisio of",a,"by",b,"is",devi)
while True:
    print("Press 1 : for addtoin")
    print("Press 2 : for subtraction")
    print("Press 3 : for multiplication")
    print("Press 4 : for divison")
    print("Press 5 : to Exit")
    ch=int(input("Enter your choise : "))
    if ch==1:
        add()
    elif ch==2:
        sub()
    elif ch==3:
        mult()
    elif ch==4:
        devi()
    elif ch==5:
        break 
    else :
        print("Invalid inpurt!")