#Variables and data types

#Inteiro (int)
idade = 21
print('Idade -', type(idade))

#Ponto Flutuante ou Decimal (float)
nota = 9.5
print('Nota -', type(nota))

#Complex
a = 5+2j
b = 20+6j

print('A -',type(a))
print('B -',type(b))
print(complex(2, 5))

#String (str)
nome = 'Cecília'
print('Nome -', type(nome))
#Boolean (bool)
fim_de_semana = True
feriado = False

print('Fim de semana - ',type(fim_de_semana))
print('Feriado -',type(feriado))
#List (list)
amigos = ['Lara', 'Silvania', 'Luis']

print('Amigos -', type(amigos))
#Tuple
idades = (20, 20, 22)

print('Idades -', type(idades))
#Dictionary (dic)

idade_amigos = {'Lara': 20, 'Silvania': 20, 'Luis': 22}

print("Idade de Amigos -", type(idade_amigos))