try:
    x = int(input('Digite um numero: '))
    y = int(input('Digite outro numero: '))
    r = x/y
except (ValueError, TypeError):
    print('Data types problem!')
except ZeroDivisionError:
    print('Division by zero problem!')
except KeyboardInterrupt:
    print('Interruption problem!')
except Exception as error:
    print(f'Excepion: {error}')
else:
    print(f'Resultado: {r}')
    print('Successfully executed')

