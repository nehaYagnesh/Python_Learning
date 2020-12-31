""" This module is to learn about data structure know as Dictionaries """

""" List : A linear collection of values that stay in order : eg. Pringles
Dictionaries : A bag of values, each with its own label """

""" Dictionaries resembles 
    Associative Arrays : Perl/PHP
    Properties or Map or HashMap - Java
    Property Bag - C#/.NET 
"""


# purse = dict()
# purse['money'] = 12
# purse['candy'] = ['Eclairs','Halls']
# purse['tissues'] = 75
# purse['candy'].append('Gems')
# print(purse['candy'])

""" Dictionary Literals (Constants)
Dictionary literals use curly braces and have a list of key :value pairs
You can make an empty dictionary using the empty curly braces
"""
# dict1 = {'notes': [2,5,100], 'candies' : ['Halls','Gems','Dairy Milk'], 'tissues' : 45}
# print(dict1)

# emptyDict = {}
# print(emptyDict)

# emptyDict2 = dict()
# print(emptyDict2)

""" Histogram : Most common name using Dictionary """
# counts = dict()
# names = ['jane','josh','jane','nick','josh','rose','jane']
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name] + 1
# print(counts)


""" Get method for dictionaries 
The pattern of checking to see if a key is already in a dictionary
and assuming a default value if the key is not there is so common that there
is a method called get() that does this for us. 

Defaults value if key does not exists (and no Traceback) """

# counts = dict()
# names = ['jane','josh','jane','nick','josh','rose','jane']
# for name in names:
#     counts[name] = counts.get(name,0) + 1 
# print(counts)


""" Counting Pattern """
# counts = dict()
# line = input('Enter a line :')
# words = line.split()
# print(f'Words: {words}')

# for word in words:
#     counts[word] = counts.get(word,0) + 1 
# print(f'Counts :{counts}')


""" Definite loops and dictionaries 
Even though dictionaries are not stored in order, we can write a for 
loop that goes through all the entries in a dictionary - actually it goes through all of the keys in the 
dictionary and looks up the values """
# dict1 = {'notes': [2,5,100], 'candies' : ['Halls','Gems','Dairy Milk'], 'tissues' : 45}
# for keys in dict1:
#     print(keys,dict1[keys])

""" Retrieving lists of Keys and Values
You can get a list of keys, values or items(both) from a dictionary """
# jjj = {'neha' : 1, 'yan' : 34, 'yag' : 100}
# print(f'List: {list(jjj)}')       # Converting the dictionary to list

# print(f'Keys of the dictionary: {jjj.keys()}') # Retriving the keys of the dictionary
# print(f'Values of the dictionary: {jjj.values()}')  # Retriving the values from the dictionary
# print(f'Items: {jjj.items()}')  # Retriving items from dictionary


""" Two Iteration Variables for Dictionaries 
We loop through the key-value pairs in a dictionary using 'two' iteration variables 
Each iteration, the first variable is the key and the second variable is the corresponding value for the key """
# jjj = {'neha' : 1, 'yan' : 34, 'yag' : 100}
# for key,value in jjj.items():
#     print(key,value)


""" Code to read the file and counts the biggest count """
# fname = input('Enter name of the file: ')
# fhandle = open(fname)

# counts = dict()
# for line in fhandle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word,0) + 1

# bigcount = None
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigcount = count
#         bigword = word
# print(f'Biggest word : {bigword} with count of {bigcount}')


