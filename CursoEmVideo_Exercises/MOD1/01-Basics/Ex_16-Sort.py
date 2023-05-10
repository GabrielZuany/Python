#Make a script to draw one of four names from a list.

from random import choice

name1 = str(input('Insert 1st name: '))
name2 = str(input('Insert 2nd name: '))
name3 = str(input('Insert 3rd name: '))
name4 = str(input('Insert 4th name: '))

list = [name1, name2, name3, name4] #Agrupa valores

drawn = choice(list)

print('The draw was {}' .format(drawn))