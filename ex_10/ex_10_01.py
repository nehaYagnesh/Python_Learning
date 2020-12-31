fname = input('Enter name of the file: ')
if len(fname) < 1 : fname = 'clown.txt'
fhandle = open(fname)

count = dict()
for line in fhandle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        count[word] = count.get(word,0) + 1
tmpsortedlist = sorted([(v,k) for k,v in count.items()],reverse=True)
for v,k in tmpsortedlist[:5]:
    print(k,v)