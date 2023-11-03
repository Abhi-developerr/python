# Write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user ..........  . 


physics = int(input("Enter marks of physics:"))
chemistry = int(input("Enter marks of chemistry:"))
math = int(input("Enter marks of math:"))
percentage = (int(physics)+int(chemistry)+int(math))/3
if (percentage>=40 and physics>=33 and  chemistry>=33 and  math>=33):
    print("you are pass ::")
else:
    print("You are fail ::")