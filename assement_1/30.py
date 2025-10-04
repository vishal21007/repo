a=0
b=1
n=int(input("Enter a number : "))
for i in range(0,n+1):
    if a>=35:
        break
    else:
        print(a,end=" ")
        a,b=b,a+b
print()