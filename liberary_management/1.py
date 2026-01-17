"""LIBERARY MANAGEMENT """
def add_book():
    Liberary={}
    n=int(input("Enter no. of books you want to add : "))
    for i in range(n):
        book_no=int(input("Entr 6 digit book code : "))
        book_nm=input("Enter book title : ")
        Liberary[book_no]=book_nm
    #adding books to liberary




#MAIN MENU
while True:
    print("1 : Add books to liberary")
    print("2 : To show books in liberary")
    print("3 : Issue books to students ")
    print("4 : To fetch issued book / student details ")
    print("5 : To del book from liberary ")
    print("6 : To add fine to student ")
    print("7 : To Exit")
    ch=int(input("Enter your choice : "))
    if ch == 1:
        ad=add_book()
        print(ad)
    elif ch ==2:
        for keys , values in dict.items(Liberary):
            
    elif ch == 7:
        break