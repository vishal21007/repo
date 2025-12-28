"""
treasure hunt finding game !!!
"""
print("Welcome to Treasure hunt !!!")
import random
lst={1:"Empty",2:"Empty",3:"Empty",4:"Empty",5:"Empty"}
ch=0
t=random.randrange(1,6)
lst[t]="Treasure"

for i in range(1,4):
    gus=int(input("Enter the hunt : "))
    for keys , values in dict.items(lst):
        if keys==gus and lst[gus]=="Treasure":
            print("you have found the tressure ")
            break
        else:
            ch=ch+1
            print(" Please try again \n you have only :",3-ch,"attempts left")
            break
if ch == 3:
    print("Sorry you died in search of tressure \n It was hidden in location : ",t )