# Reverse the entered number using loop

var=int(input("Enter a number : "))

num=0
sum=0
print('Number in reverse : ',end='')
while var > 0:
    num=var%10
    print(num,end=' ')
    var=var//10
#print("Your number is :",var)