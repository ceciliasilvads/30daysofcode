import json
from os import path

def addItem(user):
    filename = './8-14/login_system/users.json'
    listObj = []
    item = {}
    
    item['name'] = user.user_name
    item['email'] = user.email
    item['password'] = user.password
    
    if path.isfile(filename) is False:
        return False
    else:
        with open(filename, 'r') as fp:
            listObj = json.load(fp)

        listObj.append(item)
        
        with open(filename, 'w') as json_file:
            json.dump(listObj, json_file, indent=2, separators=(',',': '))
        
        return True