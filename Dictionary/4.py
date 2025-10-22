"""creat dict with name of employes and there saliry """
dic={}
n=int(input("Enter no.of employes : "))
for i in range(n):
    lst=[]
    nm=input("Enter the name of the employ : ")
    sal=int(input("Enter the saliry of the employ : "))
    lst.append(sal)
    dic[nm]=lst
print(dic)