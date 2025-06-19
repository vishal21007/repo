'''counting the face valve of number entered by the userr '''

num=int(input("Enter a number : "))
s_f=0
while num > 0:
    digit = num % 10
    s_f = s_f + digit 
    num = num // 10 
print("Face value of number is :",s_f)