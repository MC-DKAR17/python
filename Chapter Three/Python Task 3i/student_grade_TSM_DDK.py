# Danielius Karalius
# Tristan Michalek
# Real world Choice: grades
# Tristan did various small touch ups in the logic, as well as a few functions.
# I had to figure out the rest
# Figuring out the logic behind what each of the functions should do, and how we would get a maximum/minimum value from the list, but found out that there's a built in function for it

def display_menu():
    """Display the main menu options."""
    # YOUR CODE HERE
    print("1. Add a grade")
    print("2. View grade report")
    print("3. Quit")

def add_grade(grades):
    """
    Prompt for a new grade and add it to the list.
    Return the updated list.
    """
    # YOUR CODE HERE
    if 0 <= grades <= 100:
        student_grades.append(grades)
        print("Grade added!")
    else:
        print("Must require a value inbetween 0 and 100")
    

def calculate_average(grades):
    """Calculate and return the average of grades."""
    # YOUR CODE HERE
    average = sum(grades) / len(grades)
    return average
    

def get_letter_grade(average):
    """Convert numeric average to letter grade. Return the letter."""
    # YOUR CODE HERE
    if average >= 90:
        letter_grade = "A"
        return letter_grade
    elif average >= 80:
        letter_grade = "B"
        return letter_grade
    elif average >= 70:
        letter_grade = "C"
        return letter_grade
    elif average >= 60:
        letter_grade = "D"
        return letter_grade
    else:
        letter_grade = "F"
        return letter_grade

def find_highest(grades):
    """Find and return the highest grade."""
    # YOUR CODE HERE
    highest_grade = max(grades)
    return highest_grade

def find_lowest(grades):
    """Find and return the lowest grade."""
    lowest_grade = min(grades)
    return lowest_grade
    

def display_report(grades):
    """Display complete grade report with statistics."""
    # YOUR CODE HERE
    # Should show: all grades, average, letter grade, highest, lowest
    print("\nGRADE REPORT")

    print(f"\nGrades: {grades}")

    print(f"Number of assignments: {len(grades)}")

    print(f"\nAverage: {calculate_average(grades)}")

    print(f"Letter grade: {get_letter_grade(calculate_average(grades))}")

    print(f"\nHighest grade: {find_highest(grades)}")

    print(f"Lowest grade: {find_lowest(grades)}")

    


# Main program
print("=== STUDENT GRADE CALCULATOR ===")
student_grades = []

# YOUR CODE HERE - Write the main program loop
# Allow user to add grades, view report, and quit
display_menu()


while True:
    choice = int(input("\nChoice: "))
    if choice == 1:
        grades = int(input("Enter grade (0-100): "))
        add_grade(grades)
    elif choice == 2:
       display_report(student_grades)
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please choose from 1-3.")