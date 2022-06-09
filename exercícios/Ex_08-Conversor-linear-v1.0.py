#Crie um programa que leia um valor em metros e exiba ele em centimetros e milimetros 

metros = float(input('Digite um valor:'))
print('{} metros = {} cm e {} mm' .format(metros, metros*100, metros*1000))
