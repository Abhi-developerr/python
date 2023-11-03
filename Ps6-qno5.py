# Write a program to find out whether a given name is present in a list or not ..... .


lst=["abhishek","aman","pratik","rajnish","manish","sachin","rohit","akash","sunny","mohit"] 
#checking if element 7 is present
# in the given list or not
name= input("Write name here to search:")
# if element present then return
# exist otherwise not exist
if name in lst: 
    print("exist") 
else: 
    print("not exist")