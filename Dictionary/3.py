"""wap to store student information like admission no. roll no. name marks in in dictionary and 
display information on admission no. """
dic={}
n=int(input("Enter the no. of students : "))
for i in range(n):
    lst=[]
    add=int(input("Enter the admission no. : "))
    lst.append(add)
    nm=input("Enter your name : ")
    lst.append(nm)
    ro=int(input("Enter the roll no. : "))
    lst.append(ro)
    mr=int(input("Enter your marks : "))
    lst.append(mr)
    dic[add]=lst
print(dic)
ad=int(input("Enter your admission no. to get your information : "))
if ad in dic:
    print(dic[ad])
else:
    print("Invalid input !!! ")