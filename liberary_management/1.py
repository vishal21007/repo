"""LIBERARY MANAGEMENT """
Con_Liberary={482910: "The Great Gatsby",
    159302: "To Kill a Mockingbird",
    884721: "Brave New World",
    302948: "The Catcher in the Rye",
    775103: "The Hobbit",
    629405: "Nineteen Eighty-Four"}
Liberary=Con_Liberary.copy()
Book_issued={}

#MAIN MENU
while True:
    print("\n1 : Add books to liberary")
    print("2 : To show books in liberary")
    print("3 : Issue books to students ")
    print("4 : Return book ")
    print("5 : fetch issued book  ")
    print("6 : del book from liberary ")
    print("7 : To Exit")
    ch=int(input("Enter your choice : "))
    if ch == 1:
        n=int(input("Enter no. of books you want to add : "))
        for i in range(n):
            book_no=int(input("Entr 6 digit book code : "))
            book_nm=input("Enter book title : ")
            Con_Liberary[book_no]=book_nm
    #adding books to liberary
    elif ch ==2:
        print("Books available \n")
        for keys , values in Liberary.items():
            print(keys ,":",values )
        print("")
        #Displaying books 
    elif ch ==3:
        student_name=input("Enter name of the student : ")
        book_code=int(input("Enter book code to issue : "))
        student_class=input("Enter class of student : ")
        if book_code in Liberary:
            Book_issued[Liberary[book_code]]=[student_name,student_class]
            print(Liberary[book_code]," Book issued to",student_name," of ",student_class)
            Liberary.pop(book_code)
        else:
            print("Book not availabe in liberary\n")
    elif ch ==4:
        book_code=int(input("Enter book code : "))
        if book_code  in Con_Liberary:
            Liberary[book_code]=Con_Liberary[book_code]
            Book_issued.pop(Liberary[book_code])
            print("Book returned back to liberary")
        else:
            print("Book does not belong in Liberary\n")
    elif ch ==5:
        print("\nIssued books !!!")
        if len(Book_issued)==0:
            print("No book isseud right now !!!")
        else:
            for keys , values in Book_issued.items():
                print(keys," Issued to :",values)
            print("")
    elif ch ==6:
        book_code=int(input("Enter book code : "))
        if book_code in Liberary:
            del Con_Liberary[book_code]
            del Liberary[book_code]
            print("The book has been deleted ")
        else:
            print("Book not in liberayr\n")    
    elif ch == 7:
        break
    else:
        print("Invalid input !!!!")