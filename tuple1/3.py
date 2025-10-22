"""wap menu driven program of n no. of students ,
tmarks ,average , result and store them in sented tupple displY THE FOLLOWING MENU
RESULT :DISPLAY MAIN MARKS AVG RESULT(P/F)
DISPLAY : MAIN TMARKS NAME AVG
MERIT LIST : DISPLAY ALL STUDENTS GETTING AVG ABOVE 74
SEARCH : ACCEPT NAMR DISLAY DETAILS FO STUDENT  """

n=int(input("Enter no. of students : "))
tp=()
tp1()
for i in range(n):

    nm=input("Enter name of the student : ")
    tp1=tp1+(nm,)
    m=int(input("Enter total marks of the student out of 500 : "))
    tp1=tp1+(m,)
    av=(m/500)*100
    tp1=tp1+(av,)
    if av >= 33:
        tp1=tp1+("pass",)
    else:
        tp1=tp1+("Fail",)
    tp=(tp1,)
print(tp)

while True:
    print("Press 1 : DISPLAY MAIN MARKS AVG RESULT(P/F)")
    print("Press 2 : MAIN TMARKS NAME AVG")
    print("Press 3 : NAMR DISLAY DETAILS FO STUDENT")
    print("press 4 : DISPLAY ALL STUDENTS GETTING AVG ABOVE 74")
    print("press 0 : To Exit")
    ch=int(input("Enter your choise : "))
    if ch == 1 :
        for i in tp:
            print(i)
    elif ch==0:
        break
