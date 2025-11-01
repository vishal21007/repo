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

# from keys()
# dic.fromkeys(lst_keys,default_value)
keys1=[1,2,3,4]
values1="abc"
stu3=dict.fromkeys(keys1,values1)
print(stu3)

#pop item()
#removes last item and returs deleted items 
stu.popitem()
print(stu)

#max min 
print(max(stu.items()))
print(max(stu.values()))
print(max(stu))
print(min(stu.items()))
print(min(stu.values()))
print(min(stu))
print(sorted(stu))