print("===== SCHOOL MANAGEMENT SYSTEM =====")
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
        s_dict={}
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
                lst1.append(mrk)
                mrk1=int(input("Enter your marks in Maths : "))
                lst1.append(mrk1)
                mrk2=int(input("Enter your marks in science : "))
                lst1.append(mrk2)
                lst.append(lst1)
                s_dict[adsn1]=lst
        print(s_dict)
    elif ch == 5: 
        adsn1=int(input("Enter your admission number : "))
        s_dict.pop(adsn1)
    elif ch == 6 :
        for keys , values in s_dict.items():
            