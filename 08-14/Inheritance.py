class Veiculo:
    def __init__(self, marca: str, ano: str, valor: float):
        self.marca = marca
        self.ano = ano
        self.valor = valor

    def Ligar(self):
        print('O veiculo ligou!')

class Motocicleta(Veiculo):
    def __init__(self, marca: str, ano: str, valor: float, cilindradas: int):
        super().__init__(marca, ano, valor)
        self.cilindradas = cilindradas
    
    def Ligar(self):
        print('A moto ligou!')

class Aviao(Veiculo):
    def __init__(self, marca: str, ano: str, valor: float, turbinas: int):
        super().__init__(marca, ano, valor)
        self.turbinas = turbinas

    def Ligar(self):
        print('O avião ligou!')
 
veiculo1 = Veiculo('VW', '2010', 29900)
moto = Motocicleta('Honda', '2021', 2500, 200)
junkersf13 = Aviao('None', '1919', 3000000,18)

print(type(veiculo1))
print(veiculo1.ano)
veiculo1.Ligar()

print(type(moto))
print(moto.ano)
moto.Ligar()

print(type(junkersf13))
print(junkersf13.ano)
junkersf13.Ligar()