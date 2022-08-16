#Make an algorithm to read an integer number and print his double and triple, also his square root.
#Crie um algoritmo que leia um numero e mostre seu triplo, dobro e raiz.

num = int(input('Insert a number:'))
print('2x{} = {}\n3x{} = {}\nSquare root of {} = {}' .format(num, num*2, num, num*3, num, num**(1/2)))