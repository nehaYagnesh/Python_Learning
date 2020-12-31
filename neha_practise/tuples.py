""" Tuples behave just like lists 
The only difference between tuple and list is, the tuple is immutable whereas the list is mutable """

# list1 = [3, 'neha' , 12.5]
# print(list1)
# list1[1] = 'Yan'
# print(list1)

# Not possible and its gives an error
# tuple1 = (3, 'neha',12.5)
# print(tuple1)
# tuple1[1] = 'Yan'
# print(tuple1)


""" Things not to do on tuples
1. sort
2. append
3. reverse
"""
# l = list()
# print(dir(l))

# t = tuple()
# print(dir(t))



""" Tuples are comparable """

# (0,1,2) < (1,2,3) # Skips the comparision if the first item satisfies the condition


""" Sorting lists of tuples by key
We can take advantage of the ability to sort a list of tuples to get a soerted version of a dictionary
First we sort the dictionary by the key using the items() method and sorted() function """

# d = {'a' : 10 ,'b' : 1, 'c' : 22}
# d.items()
# # t = sorted(d.items())   # sorts the tuples by the key
# for k,v in sorted(d.items()):
#     print(k,v)


""" Sort by values instead of key
If we could construct a list of tuples of the form(value, key) we could sort by value
We do this with a for loop that creates a list of tuples """
# c = {'a':10, 'b': 1, 'c': 22}
# tmp = list()
# for k,v in c.items():
#     tmp.append((v,k))
# print(tmp)
# tmp = sorted(tmp,reverse= True)
# print(tmp)


""" Print top ten most commonly used words in a file """

# fname = input('Enter name of the file: ')
# fhandle = open(fname)
# count = dict()
# for line in fhandle:
#     line = line.rstrip()
#     words = line.split()
#     for word in words:
#         count[word] = count.get(word,0) + 1

# tmplist = list()    
# for key,value in count.items():
#     tmplist.append((value,key))
#     tmplist = sorted(tmplist,reverse=True)

# for val,key in tmplist[:10]:
#     print(key, val)
    

""" List comphrension : Creates a dynamic list.
In this case we make a list of reversed tuples and then sort it """

# c = {'a':10, 'b': 1, 'c': 22}
# print(sorted([(v,k) for k,v in c.items()]))

