#Generate tuples containing numbers and their cube values
# ((2,8),(3,27),(4,64))
tp=int(input("Enter the numbers : "))
lst = []
for i in range(1,tp+1):
    s=i,i**3
    lst.append(s)
tup=tuple(lst)
print(tup)  