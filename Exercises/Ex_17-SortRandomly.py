#A professor want to sort randomly presentation of works. Help him making a script to execute this task.

from random import shuffle

name1 = str(input('Insert 1st name: '))
name2 = str(input('Insert 2nd name: '))
name3 = str(input('Insert 3rd name: '))
name4 = str(input('Insert 4th name: '))

list = [name1, name2, name3, name4] #Agrupa valores

shuffle(list)

print('The presentation sort is {}' .format(list))