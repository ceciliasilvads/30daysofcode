#Repetition Structure

#For
lista = ['Ana', 'Maria', 'Lucia', 'Claudia']

for i in lista:
    print(i)

for j in range(4):
    print(j, lista[j])

for k in "Paralelepipedo":
    print(k)

for letter in 'cecilia':
    if letter == 'c' or letter == 'l':
        continue
    print('Current Letter :', letter)


#While
count = 0
while (count < 3):
    print(count, "é menor que 3")
    count = count + 1    
else:
    print(count, "é igual a 3")