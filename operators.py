#Operators

#Operadores aritméticos
print('----------------------------------------')
print('Operadores aritméticos')

A = 5
B = 3
soma = A + B
subtracao = A - B
multiplicacao = A * B
divisao = A / B
divisao_inteira = A // B
modulo = A % B
exponenciacao = A ** B

print('A =', A, 'B =', B)
print('Operação - A + B','Resultado -',soma)
print('Operação - A - B','Resultado -',subtracao)
print('Operação - A * B','Resultado -',multiplicacao)
print('Operação - A / B','Resultado -',divisao)
print('Operação - A // B','Resultado -',divisao_inteira)
print('Operação - A % B','Resultado -',modulo)
print('Operação - A ** B','Resultado -',exponenciacao)

#Operadores de atribuição
print('----------------------------------------')
print('Operadores de atribuição')

n1 = 5
n2 = 3

print('N1 =', n1, 'N2 =', n2)

n1 = 10
print('Operação - n1 = 10','Resultado -',n1)
n1 += 2
print('Operação - n1 += 2','Resultado -',n1)
n1 -= 2
print('Operação - n1 -= 2','Resultado -',n1)
n1 *= 2
print('Operação - n1 *= 2','Resultado -',n1)
n1 /= 2
print('Operação - n1 /= 2','Resultado -',n1)
n1 %= 1
print('Operação - n1 %= 1','Resultado -',n1)

#Operadores de comparação
print('----------------------------------------')
print('Operadores de comparação')

X = 1
Y = 2

print('X =', X,'Y =', Y)

print('Operação - X > Y','Resultado - ',X > Y)
print('Operação - X < Y','Resultado - ',X < Y)
print('Operação - X == Y','Resultado - ',X == Y)
print('Operação - X != Y','Resultado - ',X != Y)
print('Operação - X >= Y','Resultado - ',X >= Y)
print('Operação - X <= Y','Resultado - ',X <= Y)

#Operadores lógicos
print('----------------------------------------')
print('Operadores lógicos')

num1 = 7
num2 = 4

print('Operação - num1 > 3 and num2 < 8')
if num1 > 3 and num2 < 8:
    print('As Duas condições são verdadeiras')

print('Operação - num1 > 4 or num2 <= 8')
if num1 > 4 or num2 <= 8:
    print('Uma ou duas das condições são verdadeiras')

print('Operação - num1 < 30 and num2 < 8')
if not (num1 < 30 and num2 < 8):
    print('Inverte o resultado da condição entre os parânteses')

#Operadores de identidade
print('----------------------------------------')
print('Operadores de identidade')

lista = [1, 2, 3]
lista2 = [1, 3, 3]

# Recebe True, pois são o mesmo objeto
print('Lista 1 =', lista)
print('Lista 2 =', lista2)

print('Operação - Lista 1 IS Lista 2 Resultado -', lista is lista2)
print('Operação - Lista 1 IS NOT Lista 2 Resultado -', lista is not lista2)


#Operadores de associação
print('----------------------------------------')
print('Operadores de associação')

frutas = ['banana','laranja','uva','ameixa']
fruta_1 = 'laranja'

print('Frutas =', frutas)
print('Fruta 1 =', fruta_1)

print('Operação - Fruta 1 IN Frutas Resultado -',fruta_1 in frutas)
print('Operação - Fruta 1 NOT IN Frutas Resultado -',fruta_1 not in frutas)