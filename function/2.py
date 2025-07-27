def factorial(n):
    fact=1
    i=1
    while i<=n:
        fact=fact*i
        i=i+1
    return fact
def sum(n):
    i=1
    count=0
    o_count=0
    while i<=n:
        if i%2==0:
            count=count+i
            i=i+1
        else:
            o_count=o_count+i
            i=i+1
        
    return count,o_count
def n_sum(n):
    i=1
    cou=0
    while i<=n:
        cou=cou+i
        i=i+1
    return cou

num=int(input("Enter a number : "))
f=factorial(num)
print("Thr factrial of number is : ",f)
s,n = sum(num)
print("the sum of even number is : ",s,"\nthe sum of odd numbers is :",n)
nu=n_sum(num)
print("The sum of numbers is :",nu)