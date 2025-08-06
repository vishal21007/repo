def add(num):
    ad=num+5
    print(id(ad))

#main menu
num=int(input("Enter a number : "))
nu=add(num)
print(id(num))
print(nu)
