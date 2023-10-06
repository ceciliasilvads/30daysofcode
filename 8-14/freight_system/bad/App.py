from FreightCalculator import FreightCalculator

freight = FreightCalculator()

print('Escolha seu frete: ')
print('Express')
print('Super')
print('Super Express')
freight_option = input()
print('O frete é: R$', freight.calculate(freight_option))