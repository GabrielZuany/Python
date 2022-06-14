#Faça um programa que leia a largura e comprimento de uma parede e calcule a sua area e a quantidade de litros de tinta necessários para pintá-la, considerando que cada litro pinta 2m2 .

largura = float(input('Digite a largura da parede: '))
comprimento = float(input('Digite o comprimento da parede: '))
area = comprimento * largura

print('A area da parede é {:.2f} m^3 e será necessário {:.2f} litros de tinta para pintar.'.format(area, area/2))