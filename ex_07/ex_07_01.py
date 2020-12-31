fname = input('Enter the file\'s name: ')
try:
    fhand = open(fname)
except:
    print('Invalid file name or file cannot be found')
    quit()

for line in fhand:
    l = line.rstrip().upper()
    print(l)