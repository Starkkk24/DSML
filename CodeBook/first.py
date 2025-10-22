import json

def readFile(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

data = readFile("data.json")
# print(data)
# print(type(data))



# writing a funciton to display connecitons among the users

def displayUsers(data):
    print("Users Information:")
    for user in data['users']:
        print(f"User ID {user['id']}, {user['name']} is friends with {user['friends']} and the liked pages are {user['liked_pages']}.\n")

    print("\nPages Information:")
    for page in data['pages']:
        print(f"Page ID {page['id']} is {page['name']}.\n")

displayUsers(data)