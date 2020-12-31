import xml.etree.ElementTree as ET

# Example 1
# data = '''<person>
#     <name>Neha</name>
#     <phone type="int1">
#         +1 734 303 4456 
#     </phone>
#     <email hide="yes"/>
# </person>'''

# tree = ET.fromstring(data)
# print('Name:',tree.find('name').text)
# print('Attribute:',tree.find('email').get('hide')) 


# Example 2
data = '''<stuff>
    <users>
        <user x="2">
            <name>Nick</name>
            <id>001</id>
        </user>
        <user x="7">
            <name>Flynn</name>
            <id>002</id>
        </user>
    </users>
</stuff>'''

tree = ET.fromstring(data)
users_list = tree.findall('users/user')
for item in users_list:
    print('Name:',item.find('name').text)
    print('ID:',item.find('id').text)
    print('x:',item.get('x'),'\n')
    


    