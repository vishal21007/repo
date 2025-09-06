'''
Write a program to read email IDs of 'n' number of students and store them in a tuple. Create two new
tuples, one to store only the usernames from the email IDs and second to store domain names from
 the email IDs. Print all three tuples at the end of the program. [Hint: You may use the function split()]
'''
n=int(input("Enter the no. of students : "))
tup_email=()
tup_email_header=()
tup_email_footer=()
for i in range(1,n+1):
    email=input("Enter your email : ")
    email_header, email_footer = email.split('@')
    tup_email=tup_email+(email,)
    tup_email_header=tup_email_header+(email_header,)
    tup_email_footer=tup_email_footer+(email_footer,)
print(tup_email)
print(tup_email_header)
print(tup_email_footer)