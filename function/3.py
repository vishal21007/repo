def mode(n):
    count=0
    i=1
    x=n.sort
    while i<=len(n):
        if n[i] in x:
            count = count+1
            i = i + 1
    print("The mode of the lst is :",count )

def mean(n):
    i=1
    count=0
    while i<=len(n)-1:
        count=count+n[i]
        i=i+1
    print("The mean of the list is : ",int(count/len(n)))

def median(n):
    if len(n)%2 == 0:
        middle_value = int(len(n)/2)
    else:
        middle_value = int((len(n)+1)/2)
    n.sort()
    print('Median Value of List : ',n[middle_value])


lst=[1.4,2.4,3.5,6.9,7.3,1.4]
print(lst)
mean(lst)
median(lst)
mode(lst)