#Faça um programa que leia o salário de um funcionário e mostre seu salário com reajuste de +15%

salario = float(input('Digite o salário:'))

salario = salario*1.15

print('O valor do salario reajustado é R${:.2f}' .format(salario))