#Make a program that reads a wall's width and length, calculates your area and the quantity of ink necessary to paint it.

#Faça um programa que leia a largura e comprimento de uma parede e calcule a sua area e a quantidade de litros de tinta necessários para pintá-la, considerando que cada litro pinta 2m2 .

width = float(input('Insert the wall''s width: '))
length = float(input('Insert the wall''s length: '))
area = length * width

print('The wall''s area is {:.2f} cubic units(u^3) and will be necessary {:.2f} dm^3 of ink to paint it.'.format(area, area/2))