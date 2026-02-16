# Exercise 2 : Student Report.

def total_mark(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum

def aveg_marks(sum,length):
    if length != 0:
        avg = sum/length
        return avg
    else:
        return 0

def determine_grade(marks):
    if marks >= 90:
        return 'A+'
    elif marks > 80 and marks <90:
        return 'A'
    elif marks > 70 and marks < 80:
        return 'B'
    elif marks > 60 and marks < 70:
        return 'C'
    elif marks > 50 and marks < 60:
        return 'D'
    else:
        return 'F'

def  marks(mark_list,**subjects):
    for key, value in subjects.items():
        mark_list.append(value)



def std_report(name,roll,**subjects):
    print("="*100)
    print(" STUDENT REPORT CARD ")
    print("="*100)
    print(f"Name: {name}")
    print(f"Roll: {roll}")
    print("-"*100)
    print("Subject     Marks     Grade ")
    print("-"*100)
    for key, value in subjects.items():
        print(f"{key}          {value}         {determine_grade(value)}")
    print("-"*100)

mark_list = []
marks(mark_list,Math=85,Scie=90,Engl=78)
sum = total_mark(mark_list)
length = len(mark_list)
avg = aveg_marks(sum,length)
std_report("Arjun",101,Math=85,Scie=90,Engl=78)
print(f"Average      {avg}")
print("="*100)
print("Good Performance! Keep it up!")