# Opening the file and counting the number of lines
# xfile = open('mbox.txt')
# count = 0
# for line in xfile:
#     # print(line)
#     count += 1
# print('Line Count :',count)


# Reading the entire file at one time
# xfile = open('mbox.txt')
# inp = xfile.read()
# print(len(inp))
# print(inp[:10])


# Searching through a file
# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip()  # removes the \n at the end of the line
#     if line.startswith('Hello'):
#         print(line)  


# Skipping with continue
# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('Hel'):
#         continue
#     print(line)


# Using in to select lines
# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not 'Hello' in line:
#         continue
#     print(line)


# Prompt for file name
fname = input('Enter the file name:')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:',fname)
    quit()   # Quit enter python program execution

count = 0
for line in fhand:
    if line.startswith('Hello'):
        count +=1
print('There are',count,'hello lines in the file')

