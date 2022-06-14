#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar -----> considerando 1 real = 3.27 dólares

real = float(input('Digite o valor em reais: '))

dolar = real/3.27

print('O valor em dólares é {:.2f}'.format(dolar))