#Grading system
import random

def grade_marks(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 50:
        return "E"
    else:
        return "F"

def add_bonus(marks):
    bonus = random.randint(0, 10)
    return marks + bonus

def subtract_penalty(marks):
    penalty = random.randint(0, 5)
    return max(0, marks - penalty)

def marks_grading_system():
    student_name = input("Enter student's name: ")
    student_marks = float(input("Enter student's marks: "))

    student_marks = add_bonus(student_marks)
    student_marks = subtract_penalty(student_marks)

    grade = grade_marks(student_marks)

    print("\nStudent Name:", student_name)
    print("Original Marks:", student_marks)
    print("Grade:", grade)

marks_grading_system()