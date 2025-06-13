''''
WAP to disply sum of even numbers. ask user to enter the limt
'''

n = int(input("Enter the limt of numbers you want to print : "))
sum = 0
for i in range(n+1):
    if i%2 == 0 :
        sum = sum + i
print(sum)
