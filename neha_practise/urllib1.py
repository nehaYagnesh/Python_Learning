""" urllib in Python
Since HTTP is so common, we have a library that does all the socket 
work for us and makes web pages look like a file """

import urllib.request,urllib.parse,urllib.error

# fhandle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# count = dict()
# for line in fhandle:
#     words = line.decode().split()
#     for word in words:
#         count[word] = count.get(word,0) + 1
# print(count)

""" Reading Web Pages """
# fhand =  urllib.request.urlopen('https://www.booking.com/content/contact-us.en-gb.html') 
# for line in fhand:
#     print(line.decode().strip())





