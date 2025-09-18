# Task 1: Create a Dictionary of Student Marks

# Creating a dictionary of student marks
student_marks = {
    "Ahamed": 90,
    "Kiran": 85,
    "Sneha": 78,
    "Ravi": 92,
    "Meena": 88
}

# Asking for student name input
name = input("Enter the student's name: ")

# Retrieving marks using get() method (to avoid errors)
marks = student_marks.get(name)

# Displaying results
if marks is not None:
    print(f"{name}'s marks are: {marks}")
else:
    print(f"Student '{name}' not found in the records.")
