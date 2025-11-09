
print("===== SCHOOL MANAGEMENT SYSTEM =====")
# s_dict={admission : [name, roll_no, phn_no, english_marks, maths_marks, science_marks]}
s_dict = { 101:['abc1',1, "0123456789", 50, 60, 80],102:['abc2',2,"0123456789", 60, 65, 70],103:['abc3',3,"0123456789", 40, 50, 87] }

while True:
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Show Result Summary")
    print("7. Exit")
    ch=int(input("Enter your choice : "))
    if ch == 1 :
        n=int(input("Enter number of students : "))
        for i in range(n):
            lst=[]
            adsn=int(input("Enter your admission number : "))
            nm=input("Enter name of student : ").lower()
            lst.append(nm)
            rol=int(input("Enter your roll number : "))
            lst.append(rol)
            c_num=int(input("Enter your contact number : "))
            lst.append(c_num)
            s_dict[adsn]=lst
    elif ch == 2:
        print(s_dict)
    elif ch == 3 :
        adsn1=int(input("Enter your admission number : "))
        if adsn1 in s_dict:
            print(s_dict[adsn1])
        else:
            print("Invalid admission number !!! ")
    elif ch == 4 : 
        lst1=[]
        n=int(input("Enter no. of students you want to update marks of : "))
        for i in range(n):
            adsn1=int(input("Enter your admission number : "))
            if adsn1 in s_dict:
                mrk=int(input("Enter your marks in English : "))
                lst.append(mrk)
                mrk1=int(input("Enter your marks in Maths : "))
                lst.append(mrk1)
                mrk2=int(input("Enter your marks in science : "))
                lst.append(mrk2)
        print(s_dict)
    elif ch == 5: 
        adsn1=int(input("Enter your admission number : "))
        s_dict.pop(adsn1)
    elif ch == 6 :
        print("Name \t Roll No. \t Mobile \t English \t  Maths \t Science \t  Total marks \t Total percantage")
        for keys , values in s_dict.items():
            s=sum(values[3:5+1])
            pr=(s/300)*100
            for j in range(len(values)):
                print(values[0] ,"\t ", values[1] ,"\t ", values[2] ,"\t ", values[3] ,"\t ", values[4] ,"\t ", values[5] ,"\t ", s ,"\t ", int(pr))
                break

    elif ch==7:
        break
    else:
        print("Invalid input !!!")