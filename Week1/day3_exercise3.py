"""
Day 3: File Handling - Student data parser.
Date: February 17, 2026
Describing: Built Student data parser.
"""

# Exercise 3 : Student data.
# 1. read student data.
def read_student_data(f):
    students = []
    with open(f,'r') as  f:
        for line in f:
            line = line.strip()
            parts = line.split(',')
            name = parts[0]
            marks  = int(parts[1])
            student = {
                'name': name,
                'marks': marks
            }
            students.append(student)
    return students


    

# 2. find topper.
def find_topper(filename):
    students = read_student_data(filename)

    topper_name = ""
    highest_marks = 0
    
    for student in students:
        if student['marks'] > highest_marks:
            highest_marks = student['marks']
            topper_name = student['name']

    return highest_marks,topper_name


# 3. Student above.
def student_above_threshold(filename,threshold):
    students = read_student_data(filename)
    result = []

    for student in students:
        if student['marks'] > threshold:
            result.append(student['name'])

    return result

#  4. generate report card.
def generate_report(filename):
    students =  read_student_data(filename)

    print("="*40)
    print("Student Report")
    print("="*40)

    total_marks = 0

    for student in  students:
        name = student['name']
        marks = student['marks']

        # determining the grade.
        if marks >= 90:
            grade = 'A+'
        elif marks >= 80:
            grade = 'A'
        elif marks >= 70:
            grade = 'B'
        elif marks >= 60:
            grade ='C'
        elif marks >= 50:
            grade = 'D'
        else:
            grade = 'F'
        
        print(f"{name:<15} {marks:>5}    {grade}")
        total_marks = total_marks + marks
    average = total_marks / len(students)

    print("="*40)
    print(f"Class  Average: {average:.2f}")
    print("="*40)

filename = 'student.txt'
threshold = 85
data = read_student_data(filename)
generate_report(filename)
print(f"Topper of the Class: {find_topper(filename)}")
print("="*40)
print(f"Student above {threshold} : {student_above_threshold(filename,threshold)}")
print("="*40)
