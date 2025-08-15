
max=0
min=0
for i in range(5):
    n=int(input("Enter a number : "))
    if i==0:
        min=max=n
    if min>n:
        min=n
    if max<n:
        max=n
print(min,max)