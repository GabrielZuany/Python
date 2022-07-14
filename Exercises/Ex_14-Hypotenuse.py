#Make a scrip that reads the oposite and adjacent peccary of a triangle and print the value of his hypotenuse.
#Faça um programa que leia o cateto oposto e o catetot adjacente de um triangulo retangulo e mostre o comprimento da hipotenusa.

import math
op_peccary = float(input('Insert the oposite peccary of triangle: '))
ad_peccary = float(input('Insert the adjacent peccary of triangle: '))
hyp = pow(op_peccary, 2) + pow(ad_peccary, 2)

print('The value of hyp is {:.3f}'.format(math.sqrt(hyp)))