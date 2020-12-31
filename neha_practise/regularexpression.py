import re

""" Regular expression : search like we use find for string """
# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip()
#     if re.search('Hell',line):
#         print(line)

""" Using search() like startswith() """
# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip()
#     if re.search('^Hell',line):
#         print(line)

""" Wild card characters
/S : Refer to the documentation """


""" Matching and Extracting Data """
# x = 'My 2 favourite numbers are 19 and 43'
# y = re.findall('[0-9]+',x)
# print(y)
# z = re.findall('[AEIOU]+',x)
# print(z)


""" Greddy Matching 
The repeat characters(. and +) push outward in both directions(greedy)
to match the largest possible string """
# x = 'From: Using the : character'
# y = re.findall('F.+?:',x)  # Add a ? to be not greedy : so selects smallest string
# print(y)


""" Fine tuning string extraction 
You can refine the match for re.findall() and separately determine which 
portion of the match is to be extracted by using parantheses"""
# x = 'From neha.test@gmail.com Sat Jan  5 09:14:16 2008'
# y = re.findall('\S+@\S+',x)
# print(y)

# x= 'From neha.test@gmail.com Sat Jan  5 09:14:16 2008'
# y = re.findall('^From (\\S+@\\S+)',x)  # Match the from but only the content in the () is returned
# print(y)

# x= 'From neha.test@gmail.com Sat Jan  5 09:14:16 2008'
# y = re.findall('^From .*@([^ ]*)',x)
# print(y)

""" Spam confidence """
# fhandle = open('mbox-short.txt')
# numlist = list()
# for line in fhandle:
#     line = line.rstrip()
#     stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
#     if len(stuff) != 1 : continue
#     num = float(stuff[0])
#     numlist.append(num)
    
# print("Maximum SPAM confidence:",max(numlist))


""" Escape Character
If you want a special regular expression character to just behave
normally(most of the time) you prefix it with'\' """
# x = 'No just received $100.00 from Mike'
# y = re.findall('\$[0-9.]+',x)
# print(y)   # Output : ['$100.00']


