stu={1:"billu",2:"biddu",3:"happy",4:"singh"}
# access dictonary values 
print(stu[3])

# traversing dictionary 
for keys,values in dict.items(stu):
    print(keys,values)

#appendng values in dictonary 
po=int(input("Enter the key of new value : "))
val=input("Enter the new value : ")
stu[po]=val
print(stu)

# remove items from dictionary 
po1=int(input("Enter the key you want to del : "))
del stu[po1]
print(stu)

# / sunig pop function 
po2=int(input("Enter the key you want to del : "))
stu.pop(po2)
print(stu)

# memership operator in dictonary 
print(6 in stu)

# commom fuction 
print(len(stu))
print(stu.get(2))
print(stu.items())
print(stu.keys())

# coppy function
stu1=stu 
print(stu1)
stu2=stu.copy()
print(stu2)