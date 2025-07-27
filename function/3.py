def mean(n):
    i=1
    count=0
    while i<=len(n)-1:
        count=count+n[i]
        i=i+1
    print("The mean of the list is : ",count/len(n))
def median(n):
    me=(len(n))/2
    mee=(len(n+1))/2
    i=1
    while i<=len(n)-1:
        if i%2==0:
            print(n[me])
        
lst=[1.4,2.4,3.5,6.9,7.3,1.4]
mean(lst)
median(lst)