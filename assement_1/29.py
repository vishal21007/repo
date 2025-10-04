#fibonachi series 
a=0
b=1
n=int(input("The number of times the loop sould be done : "))
i=1
while i<=n+1:
    print(a,end=" ")
    a,b=b,a+b
    i=i+1
print()