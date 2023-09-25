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
count = 4
while (count < 3 or count > 3):
    count = count + 1
    print("Diferente de 3")
else:
    print("3")