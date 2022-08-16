#Make a script to read the wage of an emplyee and show the wage with increased by 15% .
#Faça um programa que leia o salário de um funcionário e mostre seu salário com reajuste de +15%

wage = float(input('Insert your wage:'))
wage = wage*1.15

print('The value of increased wage is U${:.2f}' .format(wage))