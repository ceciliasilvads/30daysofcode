x = 1
y = 1
z = 2
n = 3

lista = []
for i in range(x + 1): #[0, 1]
    for j in range(y + 1): #[0, 1]
        for k in range(z + 1): #[0, 1, 2]
            if (i + j + k) != n:
                lista.append([i, j, k])

print(lista)

#List comprehension

lista2 = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]
print(lista2)