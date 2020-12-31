# I
# s = 'Monty Python'
# print('Full string',s[:])
# print('First four letters:', s[0:5])
# print(s[6:])
# print(s[:4])
# print(s[:])

# Concatenation in strings
# str1 = 'Hi'
# str2 = 'Neha'
# print(str1 + ' ' + str2)

# 'in' as logical operator for strings
# fruit = 'berry'
# print('n' in fruit)
# print('e' in fruit)
# print('rry' in fruit)
# print('rrry' in fruit)

# String Library
# greet = 'Hello Neha'
# print(greet.lower())
# print(greet.upper())
# print(greet.find('el'))
# print(greet.replace('Neha','Yan'))
# print(greet.replace('e','X'))
# print(f'"{greet.lstrip()}"')
# print(f'"{greet.rstrip()}"')
# print(f'"{greet.strip()}"')
# print(greet.startswith('Hel'))
# print(greet.endswith('ha'))
# print(greet.startswith('l'))
# print(greet.endswith('f'))


# Parsing and Extracting
data = ' From neha.test@test.ca.com Sat Jan 5 09:14:16 2008'
position_at = data.find('@')
print(position_at)

position_space = data.find(' ',position_at)
print(position_space)

domain = data[position_at+1 : position_space]
print(domain)