#Build a program to read a value of standard input(Keyboard) and show all possible infos about that.
#Faça um programa que leia algo pelo teclado e imprima todas as informações possíveis sobre ela

element = input('Insert something(string, number...): ')

print('The primitive type of that element is', type(element))
print('Only have spaces?', element.isspace()) #elemento é um objeto, que possui métodos (islower, isalnum......())
print('It is a number?', element.isnumeric())
print('It is alphabetc?', element.isalpha())
print('It is alphanumeric?', element.isalnum())
print('It is uppercase?', element.isupper())
print('It is lowecase?', element.islower())
print('It is capitalized?', element.istitle())
