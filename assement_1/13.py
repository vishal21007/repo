l=int(input("please enter the length of lst : "))
lst=[]
for i in range(l):
    num=int(input("Enter the values in lst : "))
    lst.append(num)
print(lst)
print("press 1 : To edit ")
ch=int(input("Enter your choise :  "))
if ch==1:
    po=int(input("Enter the positio you want to edit : "))
    ed=int(input("Enter the change in the list : "))
    lst[po-1]=ed
    print("The updated list is",'\n',lst)
else:
    print("Invalid input !!!")
