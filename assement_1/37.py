lst=[]
n=int(input("Enter no.of students : "))
for i in range(n):
    lst1=[]
    r=int(input("Enter the roll number : "))
    lst1.append(r)
    nm=input("Enter the name of the student : ")
    lst1.append(nm)
    mr=int(input("Enter the marks of the students : "))
    lst1.append(mr)
    lst.append(lst1)
print(lst)