# +, -, *, / são os operadores básicos
# // é o operador de divisão inteira
# ** é o operador de potenciação
# % é o resto da disvisão
# == é o símbolo de igualdade

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))

print('A soma vale {}'.format(n1+n2))
print('A subtração vale {}'.format(n1-n2))
print('A multiplicação vale {}' .format(n1*n2))
print('A divisão vale {:.3f}' .format(n1/n2))#{:.nf} = n equivale ao numero de casas em ponto flutuante
print('A potencia vale {}' .format(n1**n2))
print('A divisão inteira vale {}' .format(n1//n2))
print('O resto da divisão de n1 por 2 vale {}' .format(n1%2))
print('O resto da divisao de n2 por 2 vale {}' .format(n2%2))
print('O resto da dikvisão de n1 por n2 vale {}' .format(n1%n2))