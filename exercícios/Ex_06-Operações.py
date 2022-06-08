#Crie um algoritmo que leia um numero e mostre seu triplo, dobro e raiz

num = int(input('Digite um número:'))
print('2x{} = {}\n3x{} = {}\nRaiz de {} = {}' .format(num, num*2, num, num*3, num, num**(1/2)))