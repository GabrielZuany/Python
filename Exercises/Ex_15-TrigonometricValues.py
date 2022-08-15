#Make a script to read an angle and print the correspondent trigonometric values.
#Faça um programa que leia um angulo e mostre o valor trigonometrico correspondente 

import math

angle = float(input('Insert an angle: '))

sin = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))
tan = math.tan(math.radians(angle))

print('Sin({}) : {:.2f}\nCos({}) : {:.2f}\nTan({}): {:.2f}\n' .format(angle, sin, angle, cos, angle, tan))