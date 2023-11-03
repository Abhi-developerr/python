# Write a program to find out whether a given post is talking about "Abhishek" or not ....... 


post = input("Enter a post: ")
if ("ABHISHEK" in post):
    print("Yes! the post contains the name ABHISHEK.")
elif ("abhishek" in post):
    print("Yes! the post contains the name abhishek.")
else: 
    print("No! the post does not contain the name Abhishek")