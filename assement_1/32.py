#Write a Python program to count the number of digits, letters, and special 
# characters in a given string.
str=input("Enter a string : ")
dcount=0
count=0
ccount=0
scount=0
for i in str:
    if i.isdigit():
        dcount=dcount+1
    elif i.isalpha():
        ccount=ccount+1
    elif i==" ":
        count=count+1
    else:
        scount=scount+1
print(dcount,ccount,scount)
