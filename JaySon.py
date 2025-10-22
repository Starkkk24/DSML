import json

data = {"name": "Alice", "age": 25, "city": "New York"}

dat = json.dumps(data)
print(dat) 
print(type(dat))

datt = json.loads(dat)
print(datt)
print(type(datt))

with open("jyson.json", "w") as file:
    json.dump(data, file)

with open("jyson.json", "r") as file:
   content = json.load(file)
   print(content)
   print(type(content))