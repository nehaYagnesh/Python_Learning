fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()
    words = line.split()

    # Guardian  in a compound statement
    # Short circuit evaluation 
    if len(words) < 3 or words[0] != 'From':
        continue
    print(f'Day: {words[2]}')
