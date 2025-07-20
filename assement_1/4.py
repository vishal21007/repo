# Write a program which takes two parameters : one is a string and other is a character. 
# Create a new string aer deleting all occurrences of the character from the string and return 
# the new string. 
i=0
str = "hello world"
str1 = input('enter a character : ')
str2 = len(str)-1
while i<=str2:
    if str[i]==str1:
        i = i + 1 
        continue
        
    else:
        print(str[i],end=' ')
    i = i +1