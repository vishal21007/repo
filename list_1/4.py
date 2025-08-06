#creat a list of tupple with number and their que
# output : [(1,1),(2,8,(3,27),(4,64)]

le=int(input("Enter the len of the lst : "))
lst=[]
for i in range(le):
    lst.append((i,i**3)) 
print(lst)
