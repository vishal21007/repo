n=int(input("Enter no. of students : "))
stu={}
for i in range(n):
    dic=[]
    nm=input("Enter name of the student : ")
    eng=int(input("Enter marks in eng :  "))
    dic.append(eng)
    mat=int(input("Enter marks in maths : "))
    dic.append(mat)
    scin=int(input("Enter marks in science : "))
    dic.append(scin)
    stu[nm]=dic
print(stu)

for keys,values in stu.items():
    sum=0
    for j in values:
        sum=sum+j
    print("Total marks of a student",keys,"is",sum)
    print("Percentage of student",keys,"is",int((sum/300)*100))
