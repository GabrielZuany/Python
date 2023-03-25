class Algoritmo():
    def __init__(self, tipo_algoritmo):
        self.tipo = tipo_algoritmo
        self.temporary = 0
        print("Construtor chamado para criar um objeto dessa classe")
        

alg1 = Algoritmo(tipo_algoritmo='Deep Learning')
print(hasattr(alg1, "tipo"))
print(getattr(alg1, "tipo") + "\n")

setattr(alg1, "tipo","BinaryTree")
print(getattr(alg1, "tipo") + "\n")

print(hasattr(alg1, "temporary"))
delattr(alg1, "temporary")
print(hasattr(alg1, "temporary"))