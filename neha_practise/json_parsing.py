import json

""" In JSON parsing we need to import json library. Also the JSON returns a list/dictionary once parsed """

# data = '''{
#     "name" : "Nick",
#     "phone" : {
#         "type" : "int1",
#         "number" : "+1 734 303 4456"
#     },
#     "email" : {
#         "hide" : "yes"
#     }
# }'''

# data_dict = json.loads(data)
# print('Name : ',data_dict['name'])
# print('Phone:',data_dict['phone']['number'])
# print('Attribute:',data_dict['email']['hide'])


""" Parsing a JSON : Lists with nested dictionaries """
input = '''[
            {
            "name" : "Nick",
            "phone" : {
                "type" : "int1",
                "number" : "+1 734 303 4456"
            },
            "email" : {
                "hide" : "yes"
            }
            },
            {
            "name" : "Rick",
            "phone" : {
                "type" : "int1",
                "number" : "+1 222 303 4456"
            },
            "email" : {
                "hide" : "no"
            }
            }
]'''

info = json.loads(input)
for item in info:
    print('Name',item['name'])
    print('Number', item['phone']['number'])
    print('Attribute', item['email']['hide'])