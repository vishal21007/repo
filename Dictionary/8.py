"""billing, inventory  and acc management 
wap that repeatedly ask user to enter product name and price. store all of them in pro_sales = {}
keys = product name , values = price"""

def inventory():
    n=int(input("Enter no. of products : "))
    pro_sales={}
    for i in range(n):
        nm=input("Enter product name : ")
        pri=int(input("Enter price of the product : "))
        pro_sales[nm]=pri
        return pro_sales

""" program to store details os customer name and mobile number """
def c_details():
    n1=int(input("Enter no. of customers : "))
    c_dict={}
    for i1 in range(n1):
        nm1=input("Enter name of the customer : ")
        num=int(input("Enter mobile no. of the customer : "))
        c_dict[nm1]=num
        return c_dict

"""program to search product name with the values and customer name with the mobile number"""


****** Inventory Menu ******
while True:        

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
            po=input("Enter the product name you want to search : ")
            for keys,values in inve.items():
                for j in keys:
                    if po==j:
                        print(inve[j])
        elif ch1==2:
            nm1=input("Enter name of the customer : ")
            for keys, values in cum.items():
                for j in keys:
                    if nm1==j:
                        print(cum[j])
    elif ch==4:
        
        po=input("Enter the product name you want to search : ")
            for keys,values in inve.items():
                for j in keys:
                    if po==j: