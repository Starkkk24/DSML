# People you might know

import json

data = json.load(open("data.json", "r"))

relation={}
for user in data['users']:
    relation[user['id']] = user['friends']   
# print(relation)

name={}
for user in data['users']:
    name[user['id']] = user['name']
# print(name)

for key,value in relation.items():
    for i in value:
        print(f"{name[key]} might know {name[i]}.")

