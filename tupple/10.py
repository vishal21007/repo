'''
Question 12: Advanced List Operations
Write a menu-driven program to do the various list operations:
    Sort list in ascending order
    Sort list in descending order
    Search an element
    Count an element
    Display list
'''
tup=(11,12,32,16,54,87,23,13,90)
while True:
    print("Press 1 : to arrange in ascending order ")
    print("Press 2 : to arrange is decending order ")
    print("Press 3 : to search an element ")
    print("press 4 : to count an element in tupple ")
    print("Press 5 : to Exit ")
    ch=int(input("Enter your choise : "))
    if ch == 1:
        print(sorted(tup))
    elif ch==2:
        print(sorted(tup,reverse=True))
    elif ch==3:
        s=int(input("Enter the element you want to search : "))
        if s not in tup:
            print("No its not there ")
        else:
            print("Yes it is there in the list of elements ")
    elif ch==4:
        print(len(tup))
    elif ch==5:
        break
    else:
        print("Invalid input !!!")