#Build a script that generates a random number between 0 and 5. Then, challenge the user to guess that number.
import random

#list = [0, 1, 2, 3, 4, 5]
#Rand = random.choice(list)

Rand = random.randint(0, 5)

UserNum = int(input('Try to guess the numeber (0-5): '))

if(UserNum == Rand):
    print('YOU WIN!')
else:
    print('WRONG NUMBER!\nGAME OVER\nThe number was {}'.format(Rand))