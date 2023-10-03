class Person:
  def __init__(self, name: str, age: int, profession: str):
    self.name = name
    self.age = age
    self.profession = profession

  def set_name(self, name):
    self.name = name

  def get_name(self):
    return self.name
  
  def set_age(self, age):
    self.age = age

  def get_age(self):
    return self.age
  
  def set_profession(self, profession):
    self.profession = profession

  def get_profession(self):
    return self.profession
  
  def greeting(self):
    print(f'Olá meu nome é {self.name}! Tenho {self.age} anos e minha profissão é {self.profession}.')