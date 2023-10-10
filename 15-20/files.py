arquivo = open('15-20/teste.txt', 'w', encoding="utf-8")
arquivo.write('Olá Arquivo!')
arquivo.close()

with open('15-20/teste.txt', 'a', encoding="utf-8") as arquivo2:
    arquivo2.write('\n')
    arquivo2.write('Olá arquivo denovo!')