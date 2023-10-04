class User:
    def __init__(self, user_name: str, password: str):
        self.user_name = user_name
        self.password = password
    
class System:
    def __init__(self):
        self.users_registereds = []

    def register(self, user_name: str, password: str):
        if(len(password) >= 8): 
            self.users_registereds.append(User(user_name, password))
            return True
        else:
            return False

    def login(self, user_name: str, password: str):
        for u in self.users_registereds:
            if (u.user_name == user_name and u.password == password):
                return True
            else: return False