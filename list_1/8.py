#wap to input a list and muntiply every odd no. with 3 and devide every even no. by 2 
lst=[]
n=int(input("Enter the no. of elements you want to enter : "))
for i in range(n):
    el=int(input("Enter the element : "))
    lst.append(el)
for j in lst:
    if j%2==0:
        print(j//2,end=" ")
    else:
        print(j*3,end=" ")
print()