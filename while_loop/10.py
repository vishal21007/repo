var=int(input("Enter a number : "))
print("You have entered : ",var)
num=0
while var > 0:
    num=var%10
    print(num,end=' ')
    var=var//10