from os import system


class Veiculo():
    def __init__(self, marca:str, modelo:str):
        self.__marca = marca
        self.__modelo = modelo
        
    def acelerar():
        pass

    def frear():
        pass
    
class Carro(Veiculo):
    def acelerar(self):
        print("O carro está acelerando.")
    def frear(self):
        print("O carro está freando.")

class Moto(Veiculo):
    def acelerar(self):
        print("A moto está acelerando.")
    def frear(self):
        print("A moto está freando.")
        
c = Carro("marca", "modelo")
m = Moto("MotoMarca", "MotoModelo")

c.acelerar()
m.acelerar()
        
        