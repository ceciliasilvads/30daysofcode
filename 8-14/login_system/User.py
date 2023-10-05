from add_object import addItem
import json

class User:
    def __init__(self, user_name: str, email: str, password: str):
        self.user_name = user_name
        self.password = password
        self.email = email
    
class System:
    def __init__(self):
        self.users_registereds = []

    def register(self, user_name: str, email: str, password: str):
        if(len(password) >= 8): 
            if addItem(User(user_name, email, password)):
                print('Cadastro efetuado com sucesso!')
            else:
                print('Erro no cadastro!')
            return True
        else:
            return False

    def login(self, user_name: str, password: str):
        filename = './8-14/login_system/users.json'
        
        with open(filename, 'r') as fp:
           self.users_registereds = json.load(fp)

        for i in self.users_registereds:
            if (i['name'] == user_name and i['password'] == password):
                return True