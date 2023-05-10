#Make a script to read how much money(reals) a person have in his wallet and print how much dollars she can buy (DEFINE 1 real = 3.27 dollars)

#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar -----> considerando 1 real = 3.27 dólares

real = float(input('Insert how much reals you have in your wallet: '))
dolar = real/3.27

print('You can buy {:.2f} dollars.'.format(dolar))