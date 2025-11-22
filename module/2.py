#import module to calculate import functions 
#press 1 : area of circle 
#press 2 : circum frence of circle 
#press 3 : area of rectangle 
#press 4 : perimeter of rectangle 
#press 5 : to exit

while True:
    print("press 1 : area of circle")
    print("press 2 : circum frence of circle ")
    print("press 3 : area of rectangle ")
    print("press 4 : perimeter of rectangle ")
    print("press 5 : to exit ")
    ch =int(input("Enter your choice : "))
    if ch ==1:
        r=int(input("Enter radious of circle : "))
        import math
        a=math.pi*r*r
        print("Area of circle if :",a)
    elif ch == 2:
        r=int(input("Enter radious of circle : "))
        import math
        c=math.pi*2*r
        print("Circum frence of circle is :",c)
    elif ch == 3:
        l=int(input("Enter length of the rectangle : "))
        b=int(input("Enter breath of the rectangle : "))
        a=l*b
        print("Area of rectangle is :",a)
    elif ch ==4 :
        l=int(input("Enter length of the rectangle : "))
        b=int(input("Enter breath of the rectangle : "))
        p=2*(l+b)
        print("Perimeter of rectangle is :",p)
    elif ch == 5 :
        break
    else:
        print("Invalid input !!!!!")