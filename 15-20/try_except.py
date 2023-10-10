try:
    with open('15-20/teste3.txt', 'w') as f:
        f.write('My programmatically created file!')
except FileNotFoundError:
    print('The file does not exist')