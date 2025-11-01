"""billing, inventory  and acc management 
wap that repeatedly ask user to enter product name and price. store all of them in pro_sales = {}
keys = product name , values = price"""

def inventory():
    n=int(input("Enter no. of products : "))
    pro_sales={}
    for i in range(n):
        nm=input("Enter product name : ").lower()
        pri=int(input("Enter price of the product : "))
        pro_sales[nm]=pri
    return pro_sales

""" program to store details os customer name and mobile number """
def c_details():
    n1=int(input("Enter no. of customers : "))
    c_dict={}
    for i in range(n1):
        nm1=input("Enter name of the customer : ").lower()
        num=int(input("Enter mobile no. of the customer : "))
        if len(num)==10:
            c_dict[nm1]=num
        else:
            print("Invalid mobile no. !!!")
    return c_dict

"""program to search product name with the values and customer name with the mobile number"""



while True:        
    print("****** Inventory Menu ******")
    print("Press 1 : Inventory Entires (Products)")
    print("Press 2 : Enter Customer Detail")
    print("Press 3 : Search Product or Customer Details")
    print("Press 4 : Billing")
    print("Press 5 : Exit")
    ch=int(input("Enter your choice : "))
    if ch == 1:
        inve = inventory()
        print(inve)
    elif ch == 2:
        cum = c_details()
        print(cum)
    elif ch == 3:
        print("press 1 : to get product details  ")
        print("press 2 : to get customer details ")
        ch1=int(input("Enter your choice : "))
        if ch1==1:
            po=input("Enter the product name you want to search : ").lower()
            for keys,values in inve.items():
                if po in keys:
                    print(inve[po])
        elif ch1==2:
            nm1=input("Enter name of the customer : ").lower()
            for keys, values in cum.items():
                if nm1 in keys:
                    print(cum[nm1])
    elif ch==4:
        sum=0
        n1=int(input("Enter no. of different product : "))
        for i in range(n1):
            po=input("Enter the product name you want to search : ").lower()
            no1=int(input("Enter no. of products : "))
            for keys,values in inve.items():
                if po in keys:
                    value = inve[po]
            sum = sum + (value*no1)
            print("Total values is : ",values*no1)
        print("Total amount is  : ",sum)
    elif ch==5:
        break
    else:
        print("Invalid input !!!")