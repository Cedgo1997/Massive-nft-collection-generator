import json

def Save(name, data):
    with open(name + '.json', 'w') as file:
        json.dump(data.__dict__, file, indent=4)