import math

# Not a 'Collection' : Most of our variables have one value in them - when we put a new value
# in the variable, the old value is overwritten


""" Collection : Allows the user to put many values in a single variable
 """
# friends = ['Nick','Rick','Mike']
# for friend in friends:
#     print('Hey',friend)


""" Looking inside lists """
# friends = ['Nick','Rick','Mike']
# print(friends[1])

""" Lists are mutable
Strings are immutable - we cannot change the contents of a string - we must make a new string to make any change
List are mutable -> We can change an element of a list using the index operator """
# lotto = [2,14,26,41,63]
# print(lotto)
# lotto[2] = 28
# print(lotto)


""" Length of list """
# friends = [0,'Nick','Rick','Jake']
# print(len(friends))


""" Using the range function
The range function returns the list of numbers that range from zero to one less than the parameter
We can construct an index loop using for and an integer iterator """
# friends = ['Nick','Rick','Mike']
# for i in range(len(friends)):
#     friend = friends[i]
#     print('Hey',friends)


""" Concatenating lists using +
We can create a new list by adding two existing lists together """
# list1 = [1,3,4]
# list2 = [5,7,0]
# list3 = list1 + list2
# print(list3)

""" Slicing the list using :
Up to but not including """
# list1 = [1,2,3,4,5,6,7,8,9,0]
# list2 = list1[1:3]
# print(list2)
# list3 = list1[:4]
# print(list3)
# list4 = list1[3:]
# print(list4)


""" List methods
1. append : List elements are added at the end of the list """
# stuff = list()  # create an new empty list
# stuff.append('book')
# stuff.append(0)
# print(stuff)

""" 2. 'in' and 'not in' : Checks if an item is present/not present in the list
These operators don't change the list  """
# somelist = [1,3,9,21,10,16]
# print(9 in somelist)
# print(15 not in somelist)
# print(3 not in somelist)

""" 3. Sorting the list elements
A list can be sorted using 'sort' method """
# friends = ['Gima','Sita','Ash']
# friends.sort()
# print(friends) 

""" 4. Built-in functions for lists
len, min, max, sum """
# nums = [3,41,12,9,74,15]
# print('Length of nums:',len(nums))
# print('Min in nums:',min(nums))
# print('Max in nums',max(nums))
# print('Sum of all elements in nums:',sum(nums))
# print('Average of all elements in nums:',format(sum(nums)/len(nums),'.2f'))


""" Rewriting the code to calculate the average of numbers input by the user
Refer ex_05_01.py in folder 'ex_05' """
# numlist = list()
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done':
#         break
#     value = float(inp)
#     numlist.append(value)

# average = sum(numlist)/len(numlist)
# print('Average:',average)


""" Split : Breaks a string into parts and produces a list of strings.We think of these as words.
We can access a particular word or loop through all the words. """
# splitstuff = 'Welcome to Canada'
# splitlist = splitstuff.split()
# print(splitlist[2])
# print(len(splitlist))
# for word in splitlist:
#     print(word)


""" Delimiter
When you do not specify a delimiter, mulitple space are treated like one delimiter
You can specify what delimiter character to use in the splitting """
# line = 'A lot        of spaces'
# etc1 = line.split()
# print(etc1)

# line = 'first;second;third'
# etc = line.split()
# print(f'Length:{len(etc)} and etc list : {etc}')
# etc_2 = line.split(';')
# print(f'Length:{len(etc_2)} and etc list : {etc_2}')

""" The Double Split Patter
 Sometimes we split a line one way, and then grab one of the pieces
of the line and split that piece again"""
# str1 = 'From neha.test@gmail.test Sat Jan 5 09:14:16 2008'
# words = str1.split()
# email = words[1]
# emailList = email.split('@')
# domain = emailList[1]
# print(f'Domain is {domain}')

