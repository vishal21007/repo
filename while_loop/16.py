a = 3
for i in range(a,a<100):
    if i%2 == 0:
        print(i+2,end=',')
    else:
        print(i*2,end='$')
    i = i + 3
