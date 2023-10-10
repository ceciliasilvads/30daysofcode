file_name = input('Nome do arquivo: ')
title = input('Título da nota: ')
content = input('Conteudo da nota: ')

try:
    with open(f'15-20/ {file_name}.txt', 'a') as f:
        f.write(title)
        f.write('\n')
        f.write(content)
except FileNotFoundError:
    print('The file does not exist!')