'''
print all odd numbers from n-m ask user to enter both n and m 
'''
n=int(input("Enter the stating point : ")) # 10
m=int(input("Enter the end point : ")) # 20

while n<=m:
    if n%2 == 1:
        print(n,' is odd')
    n = n + 1