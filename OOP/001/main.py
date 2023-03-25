
class Livro():
    # esse método instancia um objeto criado a partir dessa classe
    # (self) é uma referência a cada atributo da própria classe (e não de uma classe mãe, por exemplo)
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print("Construtor chamado para criar um objeto dessa classe")
        
    # métodos são funções que atuam sobre os objetos da classe.
    def imprime(self):
        print(f"Registrado o livro {self.titulo} com ISBN '{self.isbn}'")
    

livro1 = Livro("O Poder do Hábito", 9998888)
livro1.imprime()

