
# asking for the name of the student
student_name = input("Student name: ")

# setting up empty variables to store the grades and subjects from the for loop
subjects = []
grades = []

# asking the user five times, for a subject, and then a grade, and then both items get added to the arrays.
for i in range(1, 6):
    subject = input(f"Enter subject {i}: ")
    grade = int(input(f"Enter grade {i}: "))
    subjects.append(subject)
    grades.append(grade)

# using \n to make the output look a little cleaner with a line break.
print("\n REPORT CARD")
print(f"Student: {student_name}")

# \n being using again.
print("\n")

# printing out the values from the arrays.
for i in range(5):
    print(f"{subjects[i]} grade is {grades[i]}")

# calculating the average grade amongst the five.
average_grade = sum(grades) / 5

# printing out the average grade.
print(f"\n Average grade: {average_grade}")

# conditional statements that determine the type of letter grade the student gets
if average_grade >= 90:
    print("Letter grade: A")
elif average_grade >= 80:
    print("Letter grade: B")
elif average_grade >= 70:
    print("Letter grade: C")
elif average_grade >= 60:
    print("Letter grade: D")
else:
    print("Letter grade: F")