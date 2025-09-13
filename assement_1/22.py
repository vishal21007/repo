#wap to take a string from the user abd replace Every blank spacewith (#)
str=input("Enter a string : ")
for i in str:
    if i==" ":
        print("#",end=" ")
    else:
        print(i,end="")
print()