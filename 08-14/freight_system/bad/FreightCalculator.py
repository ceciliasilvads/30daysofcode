from typing import Final
from FreightExpress import FreightExpress
from FreightSuper import FreightSuper
from FreightSuperExpress import FreightSuperExpress

EXPRESS: Final[str] = 'express'
SUPER: Final[str] = 'super'
SUPER_EXPRESS: Final[str] = 'super express'

class FreightCalculator:
    def __init__(self) -> None:
        pass

    def calculate(self, freight_option: str):
        freight = None

        if (freight_option.lower() == EXPRESS.lower()):
            freight = FreightExpress()
        elif (freight_option.lower() == SUPER.lower()) :
            freight = FreightSuper()
        elif (freight_option.lower() == SUPER_EXPRESS.lower()) :
            freight = FreightSuperExpress()
        else: raise ValueError("Invalid Argument")      

        return freight.getValue()