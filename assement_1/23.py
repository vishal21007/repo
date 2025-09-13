#Write a program to check whether the string is a palindrome or not
str=input("Enter a name : ")
str1=str[::-1]

if str==str1:
    print("Yes its a palindrom ")
else:
    print("No its not a palindrom")