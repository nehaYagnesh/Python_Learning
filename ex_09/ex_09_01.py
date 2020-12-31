fname = input('Enter name of the file: ')
if len(fname) < 1 : fname = 'clown.txt'
fhandle = open(fname)

for line in fhandle:
    line = line.rstrip()
    words = line.split()

    count = dict()
    for word in words:
        count[word] = count.get(word,0) + 1
    
    biggestWord = None
    biggestCount = None
    for word,count in count.items():
        if biggestCount is None or count > biggestCount:
            biggestCount = count
            biggestWord = word
print(f'Biggest word is "{biggestWord}" with count {biggestCount}')
        



