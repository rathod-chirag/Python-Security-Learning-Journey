# Day 4 - Learning File writing.
# Date: 18-feb-2026

# 1. Writing the  data in a file using the 'w' mode.
with open('output.txt','w') as file:
    file.write("Hello, I am learning the writing mode of the file.\n")


# 2. Appending content to a file.
with open('output.txt','a') as file:
    file.write("This is new content, written in appending mode.\n")

# 3. Writing the multiple files in a file.
lines = ["First line\n","Second line\n","Third line\n"]
with open('output.txt','a') as file:
    file.writelines(lines)

# Displaying the data of the file after writing the data in a file.
with open('output.txt','r') as file:
    content = file.read()
    print(content)
