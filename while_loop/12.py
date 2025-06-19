''' 1234 : 4 digit number entered, 345 -> 3 digit number entered  '''

num=int(input("Enter a number : "))

count=0
i=num
while num > 0:
    count = count + 1
    num = num // 10
print(count)
