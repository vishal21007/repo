n=int(input("Enter a number : "))
sum=0
for i in range(1,n+1):
    val=1/(i**3)
    sum=sum+val
print(sum)