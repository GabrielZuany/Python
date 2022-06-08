#faça um programa que leia algo pelo teclado e imprima todas as informações possíveis sobre ela

elemento = input('Digite algo: ')

print('O tipo primitivo desse dado é', type(elemento))
print('Só tem espaços?', elemento.isspace()) #elemento eh um objeto, que possui métodos (islower, isalnum......())
print('É número?', elemento.isnumeric())
print('É alfabético?', elemento.isalpha())
print('É alfanumerico?', elemento.isalnum())
print('Está em maiúsculas?', elemento.isupper())
print('Está em minúsculas?', elemento.islower())
print('Está capitalizada?', elemento.istitle())
