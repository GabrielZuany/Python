class Figura():
    def __init__(self) -> None:
        pass

    def area(self):
        pass
    
    def imprimetipo(self):
        print(type(self))
    
class Quadrado(Figura):
    def __init__(self, lado):
        Figura.__init__(self)
        self.lado = lado
        print("Objeto quadrado criado!")
        
    def area(self)->float:
        return self.lado*self.lado
    

q = Quadrado(5)
print(q.area())
print(q.imprimetipo())