#compilar no terminal------> python3 nome_arquivo.py

print("Hello World!")
print(7+4)#operação de soma
print("7"+"4")#operação de concatenação
print("ola", 5)#as vezes a virgula funcion melhor que o + 

#\n é quebra de linha

nome = input('Digite seu nome: ')
print('Prazer em te conhecer {:20}!' .format(nome))
print('Prazer em te conhecer {:>20}!' .format(nome))
print('Prazer em te conhecer {:<20}!' .format(nome))
print('Prazer em te conhecer {:^20}!' .format(nome), end=' ')#esse end junta a proxima linha, eliminando a quebra de linha
print('Prazer em te conhecer {:=^20}!' .format(nome))
