# Write a program to provide grade according to marks

marks = float(input("Enter Marks from 1 to 100"))

if (100 >= marks > 90):
    print("Grade A")

elif (marks > 70):
    print("Grade B")

elif (marks > 50):
    print("Grade C")

elif (marks >= 35):
    print("Grade D")

elif (marks < 35):
    print("Your are Fail")

else:
    print("Enter Valid Number of Marks")
