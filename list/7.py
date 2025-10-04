#wap a menu driven program to perform various operaions 
# opt1 append element in a list 
# opt2 insert elemet 
# opt3 append a list to given list 
# opt4 modiefy element 
# opt5 del element from its position 
# opt6 del element with given valu
# opt7 sort the list in assending 
# opt8 sort the list in decending
# opt9 display the list 
# opt10 exit
lst=[24,4,16,38,13]

#menu
while True:
    print("Press 1 : to append element in a list ")
    print("press 2 : to insert elemet ")
    print("press 3 : to append a list to given list ")
    print("press 4 : to modiefy element ")
    print("press 5 : to del element from its position ")
    print("press 6 : to del element with given value ")
    print("press 7 : to sort the list in assending ")
    print("press 8 : to sort the list in decending ")
    print("press 9 : to display the list ")
    print("press 0 : to Exit ")
    ch=int(input("Enter your choise : "))
    if ch == 1:
        n=int(input("Enter a no. you want to append : "))
        lst.append(n)
        print("Element has been appended ")
    elif ch==2:
        n=int(input("Enter a no. you want to insert : "))
        po=int(input("Enter the position you want to insert in : "))
        lst.insert(po-1,n)
        print("Element has been inserted")
    elif ch==3:
        lst1=[]
        n=int(input("Enter the no. of elements you want in your list : "))
        for i in range(n):
            nu=int(input("Enter a no. you want to append : "))
            lst1.append(nu)
            lst.extend(lst1)
            print("list has been extended ")
    elif ch==4:
        n=int(input("Enter a no. you want to insert : "))
        po=int(input("Enter the position you want to insert in : "))
        lst[po-1]=n
        print("the list has got changed ")
    elif ch==5:
        po=int(input("Enter the position you want to delet : "))
        if po<len(lst):
            lst.pop(po-1)
            print("the element has been deleted ")
        else:
            print("Invalid index value !!!")
    elif ch==6:
        n=int(input("Enter the element you want to delet : "))
        if n in lst:
            lst.remove(n)
            print("The element has bee deleted")
        else:
            print("Invalid input !!!")
    elif ch==7:
        lst.sort()
        print(lst)
    elif ch==8:
        lst.sort(reverse=True)
        print(lst)
    elif ch == 9:
        print(lst)
    elif ch == 0:
        break

