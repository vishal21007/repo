#n=int(input("Enter the limit for loop : "))
a=0
b=1
for i in range(5):
    print(a, end=' ')
    a,b=b,a+b
print('')