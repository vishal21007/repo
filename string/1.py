# using while print input string in reverse

str=input("Enter a sting : ")

for i in range(len(str)-1,-1,-1): # range(5,0,-1)
    print(str[i])