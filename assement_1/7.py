def su(n):
    count=0
    for i in range(1,n+1):
        count = count + i
    print(count)
#main menu 
n=int(input("Enter a number : "))
su(n)