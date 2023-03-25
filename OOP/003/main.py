class Circulo():
    
    PI = 3.141592
    
    def __init__(self, raio:float = 1)->None:
        # __ antes das variaveis as tornam privadas, de modo que apenas a classe pode acessá-la
        self.__raio = raio
    
    def area(self)->float:
        return (self.__raio*self.__raio) * Circulo.PI
    
    def setraio(self, raio:float)->None:
        self.__raio = raio
    
    def getraio(self)->float:
        return self.__raio

circulo1 = Circulo(2)
print(circulo1.area())
    