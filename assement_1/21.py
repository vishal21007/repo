# wap to count and display the num of values divisible
# by 8 in lst numberList with n num of elements entered by the user
n=int(input("Enter how many num you want to enter : "))
count=0
lst=[]
for i in range(1,n+1):
    num=int(input("Enter the number : "))
    if num%8==0:
        lst.append(num)
        count=count+1
    else:
        continue
print(lst,count)
