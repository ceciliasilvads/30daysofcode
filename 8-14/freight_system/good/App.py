from FreightCalculator import FreightCalculator
from FreightExpress import FreightExpress
from FreightSuper import FreightSuper
from FreightSuperExpress import FreightSuperExpress
from typing import Final

EXPRESS: Final[str] = 'express'
SUPER: Final[str] = 'super'
SUPER_EXPRESS: Final[str] = 'super express'
freight_calculator = FreightCalculator()

print('Escolha seu frete: ')
print('Express')
print('Super')
print('Super Express')
freight_option = input()

freight = None

if (freight_option.lower() == EXPRESS.lower()):
    freight = FreightExpress()
elif (freight_option.lower() == SUPER.lower()) :
    freight = FreightSuper()
elif (freight_option.lower() == SUPER_EXPRESS.lower()) :
    freight = FreightSuperExpress()
else: raise ValueError("Invalid Argument")

print('O frete é: R$', freight_calculator.calculate(freight))