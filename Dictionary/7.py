"""wap to input names of n employes and there saliry [basic , house rent , allowanvce ] calculate total salary 
display the salary"""
dic={}
n=int(input("Enter the no. of employes : "))
for i in range(n):
    lst=[]
    nm=input("Enter the name of the employ : ")
    ba=int(input("Enter your basic salary : "))
    lst.append(ba)
    hr=int(input("Enter your house rent : "))
    lst.append(hr)
    alow=int(input("Enter your allowance : "))
    lst.append(alow)
    dic[nm]=lst

for keys,values in dic.items():
    sum=0
    for i in values:
        sum=sum+i
    dic[keys]=sum
print(dic)

