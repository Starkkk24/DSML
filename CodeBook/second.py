# Cleaning Data


import json

def loadData(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data

data = loadData("data2.json")

def cleanData():
    data['users'] = [user for user in data['users'] if user['name'].strip()]

    for user in data['users']:
        user['friends'] = list(set(user['friends']))

    data['users'] = [user for user in data['users'] if user['friends'] or user['liked_pages']]

    uniquePages = {}
    for page in data['pages']:
        uniquePages[page['id']] = page
    data['pages'] = list(uniquePages.values())
    return data



data = cleanData()
json.dump(data, open("Clean_data2.json", "w"), indent=2)
print("Data has been Cleaned successfully!")

