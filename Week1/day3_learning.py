# File I/O in python.

# Methods of opining a file in different formate.
# 'r' - open file for reading (default)
# 'w' - open file for writing, truncating the file first.
# 'x' - create a new file and open in for writing.
# 'a' - open for writing, appending to the end of the file if it exist.
# 'b' - binary mode.
# 't' - text  mode(default)
# '+' - open a disk file for updating (raeading and writing)

# 1. Opining a file in read mode and reading the content of the file.
f = open('myfile.txt','r')

# Reading the content of the file.
text = f.read()
# Reading the content line by line.
line1 = f.readline()
line2 = f.readline()

# Displaying the content of the file.
print(text) 
print(line1)
print(line2)

# Closing the file.
f.close()

# 2. Opining a file in a writing mode.

f = open('demo.txt','w')
f.write("This is a new content.")
f.close()


# 3. r+ reading  and writing the file content.
f = open('demo.txt','w+')
f.write("hello world.")
data = f.read()
print(data)
f.close()

# 4. with syntax.

with open('demo.txt','r') as f:
    data = f.read()
    print(data)

with open('demo.txt','w') as f:
    f.write("Hello Coders.")

# 5. Creating the file and adding the data in it.
f = open('demo1.txt','x')
f.write("Hey, how are you.")
f.close()