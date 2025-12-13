# create a dictionary, holding values - emp id, secret_code(5 digits), name, desgination. print values of all emp.
import random

n=int(input("Enter the no. employs data you want to enter : "))
dic={}

for i in range(n):
    eml=input("Enter your emp id : ")
    for j in range(5):
        c=random.random()
        code=c*100000

    nm=input("Enter your name : ")
    desig=input("Enter your designation : ")
    dic[eml]=[int(code),nm,desig]
print(dic)