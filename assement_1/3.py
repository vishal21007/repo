#6. Write a program to check if a string is a palindrome or not. 
# (A string is called palindrome if it reads same backwards as forward. For example, Kanak is a palindrome.)
str=input("Enter a name : ")
str1=str[::-1]
flag = True
for i in range((len(str))-1):
    if str[i] != str1[i]:
        print('This is not a palindrome')
        flag = False
        break

if flag: # if flag == True
    print('This is a palindrom.')