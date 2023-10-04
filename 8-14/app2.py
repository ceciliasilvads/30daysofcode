from User import System
import os

system = System()

def register():
    print('----------------------- CADASTRO -----------------------')
    nome = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')

    isRegisteredSussesfully = system.register(nome, senha)

    if isRegisteredSussesfully:
        os.system('cls')
    else: print('O cadastro falhou!')

def login():
    print('------------------------ LOGIN -------------------------')
    user_name = input('Digite seu nome de usuário: ')
    password = input('Digite sua senha: ')

    if system.login(user_name,password):
        print('login efetuado com sucesso!')
    else:
        print('O login falhou!')

def sistema_app():
    register()
    login()


if __name__ == '__main__':
    sistema_app()