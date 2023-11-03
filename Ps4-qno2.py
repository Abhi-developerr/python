#  write a program to accept marks of 6 students and display them in a sorted manner . . . . .  


m1 = int(input("Marks of 1st student : "))

m2 = int(input("Marks of 2nd student : "))

m3 = int(input("Marks of 3rd student : "))

m4 = int(input("Marks of 4th student : "))

m5 = int(input("Marks of 5th student : "))

m6 = int(input("Marks of 6th student : "))

SortedMarks = [m1, m2, m3, m4, m5, m6]

SortedMarks.sort()

print(SortedMarks)