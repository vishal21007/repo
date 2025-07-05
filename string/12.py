#factorial
i=1
fact = 1
x=int(input("Enter the number you want to get factorial for : "))
while i<=x:
    fact = fact * i
    i = i + 1
print("Factorial of no.",x,'is : ',fact)