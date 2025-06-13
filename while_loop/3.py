'''
print factorial of 5! = fact=i*fact (1x2x3x4x5)
'''
i = 1
fact=1
n = int(input('Enter value to calculate factorial of : '))

while i<=n:
    fact = fact*i
    i = i + 1

print('Factorial : ',fact)