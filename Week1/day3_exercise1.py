# Exercise 1 : File Statistics

# 1. count lines
def count_lines(filename):
    f = open(filename,'r')
    data = f.readline()
    line_count = 0
    while data:
        line_count += 1
        data = f.readline()
    
    f.close()
        
    return line_count

# 2. count words
def count_words(filename):
    f = open(filename,'r')
    data = f.read()
    lis = data.split()
    count = len(lis)
    f.close()
    return count


# 3. find longest line 
def longest_line(filename):
    f = open(filename,'r')
    longest = 0
    line = 1
    l = 0
    data = True
    while data:
        data = f.readline()
        if len(data) > longest:
            longest = len(data)
            l = line
        line = line + 1
    f.close()
    return l


    

filename = 'sample.txt'
print(count_lines(filename))
print(count_words(filename))
print(longest_line(filename))
