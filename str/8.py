str=input("Enter a string : ")
alp=0
dig=0
sym=0
spa=0
for i in str:
    if i.isalpha():
        alp=alp+1
    elif i.isdigit():
        dig=dig+1
    elif i.isspace():
        spa=spa+1
    else:
        sym=sym+1
print("no. of alphabets : ",alp)
print("no. of digits : ",dig)
print("no. of special symbols : ",sym)
print("no. of words in the str : ",len(str.split()))
print("Lenght of string is : ",len(str))