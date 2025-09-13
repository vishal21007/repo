#Create a function to sum all digits in a string.
str=input("Enter a string : ")
count=0
for i in str:
    if i.isdigit():
        a=int(i)
        count=count+a
print(count)