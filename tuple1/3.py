"""wap menu driven program of n no. of students ,
tmarks ,average , result and store them in sented tupple displY THE FOLLOWING MENU
RESULT :DISPLAY MAIN MARKS AVG RESULT(P/F)
DISPLAY : MAIN TMARKS NAME AVG
MERIT LIST : DISPLAY ALL STUDENTS GETTING AVG ABOVE 74
SEARCH : ACCEPT NAMR DISLAY DETAILS FO STUDENT  """

n=int(input("Enter no. of students :"))
tp=()
for i in range(1,n+1):
    tp1=()
    ro=int(input("Enter roll number of the student ",i,":"))
    tp1=tp1+(ro,)
    nm=input("Enter name of the student ",i,": ")
    tp1=tp1+(nm,)
    m=int(input("Enter total marks of the student out of 300 : "))
    tp1=tp1+(m,)
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
        for j in tp:
            if type(j)==int:
                if j/300<93:
                    print("Student",j,"is pass")
                else:
                    print("Student",j,"is Fail")
            else:
                continue