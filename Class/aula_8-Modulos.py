import math

num = int(input('Digite um número:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {} arredondando para cima.'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {} arredondando para baixo.'.format(num, math.floor(raiz)))