#functions
def reverte_string(mensagem):
    print(mensagem[::-1])
        

def calcula_fatorial(number):
    if number == 0:
        return 1
    else:
        return number * calcula_fatorial(number-1)

if __name__ == '__main__':
    print(calcula_fatorial(20))
    reverte_string('12345')