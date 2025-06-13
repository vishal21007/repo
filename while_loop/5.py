# input 2 (starting, ending) values from users and calculate avg.

st=int(input("Enter the starthing point : ")) # 10
en=int(input("Enter the ending point : ")) # 20
diff = en - st # 20 - 10 = sum/10
sum=0
while st<=en:
    sum = sum + st
    st = st + 1
print(sum/diff)
