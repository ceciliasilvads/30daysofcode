class Veiculo:
    def __init__(self, marca: str, ano: str, valor: float):
        self.marca = marca
        self.ano = ano
        self.valor = valor

class Motocicleta(Veiculo):
    def __init__(self, marca: str, ano: str, valor: float, cilindradas: int):
        super().__init__(marca, ano, valor)
        self.cilindradas = cilindradas

class Aviao(Veiculo):
    def __init__(self, marca: str, ano: str, valor: float, turbinas: int):
        super().__init__(marca, ano, valor)
        self.turbinas = turbinas
 
veiculo1 = Veiculo('VW', '2010', 29900)
moto = Motocicleta('Honda', '2021', 2500, 200)
junkersf13 = Aviao('None', '1919', 3000000,18)

print(type(veiculo1))
print(veiculo1.ano)

print(type(moto))
print(moto.ano)

print(type(junkersf13))
print(junkersf13.ano)