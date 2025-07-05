# input string from user, and print string in upper/lower intermittently.
# input = hello, output = HeLlO
var=input("Enter a string : ")
for i in range(len(var)):
    if i%2==0:
        print(var[i].upper(),end=' ')
    else:
        print(var[i].lower(),end=' ')
print()