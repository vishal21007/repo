lst=[]
ls=int(input("Enter the len of the list : "))
for i in range(ls):
    inn=input("Enter the list you want to append : ")
    lst.append(inn)
print("Elements in the list :",lst)
while True:
    print("press 1 : to Append an element")
    print("press 2 : to Insert an element")
    print("press 4 : to Modify an existing element")
    print("press 5 : to Delete an existing element from its position")
    print("press 7 : to Sort the list in ascending order")
    print("press 0 : to exit ")
    ch=int(input("Enter your choise : "))
    if ch==1:
        a=input("Enter the elemet you want to add : ")
        lst.append(a)
        print("The updated list :",lst)
    elif ch==2:
        po=int(input("Enter the idex you want to change : "))
        el=input("Enter the element you want to change : ")
        lst.insert(po-1,el)
        print("The updated list is :",lst)
    elif ch==4:
        po=int(input("Enter the idex you want to change : "))
        el=input("Enter the element you want to change : ")
        pos=po-1
        lst[pos]=el
        print("The updated list : ",lst)
    elif ch==5:
        po=input("Enter the element you want to remove : ")
        lst.remove(po)
        print("The updated list : ",lst)
    elif ch==7:
        lst.sort()
        print(lst)
    elif ch==0:
        break
    else:
        print("Invalid value !!")