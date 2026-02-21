"""
Day 3: File Handling - Reading the files.
Date: February 17, 2026
Describing: Learninng to  read files.
"""

# Exercise 2 : Numbers File.
# 1. read numbers.
def read_num(f):
    f = open(f,'r')
    data = True
    while data:
        data = f.readline()
        print(data)
    f.close()

# 2. sum form  file.
def sum_from_file(f):
    f = open(f,'r')
    data = f.read()
    num = data.split()
    sum = 0 
    for i in num:
        sum = sum + int(i)

    f.close()
    return sum


# 3. max and min 

def max_min(li):
    max_num = max((li))
    min_num = min((li))
    return max_num, min_num

f = 'numbers.txt'
print("numbers present in the file.")
read_num(f)
print(f"Sum of the numbers of a file : {sum_from_file(f)}")

f = open(f,'r')
data = f.read()
li = data.split()
print(f"Max and Min of the file : {max_min(li)}")