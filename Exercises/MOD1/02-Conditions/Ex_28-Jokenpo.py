#Make a Jokenpo minigame.   
from random import choice
from time import sleep

list = ['sissors', 'rock', 'paper']
Rand = choice(list)

option = int(input('1)sissors\n2)rock\n3)paper\n'))
flag = 1 #if user choose an invalid option

if option == 1:
    UserChoice = 'sissors'
elif option == 2:
    UserChoice = 'rock'
elif option == 3:
    UserChoice = 'paper'
else:
    flag = 0


if flag == 1:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!\n')
    sleep(0.5)
    print('-='*10)

    if UserChoice == Rand:
        print('You: {}\nComputer: {}'.format(UserChoice, Rand))
        print('Draw!')
    elif (Rand == 'rock' and UserChoice!='paper') or (Rand == 'paper' and UserChoice!='sissors') or (Rand == 'sissors' and UserChoice!='rock'):
        print('You: {}\nComputer: {}'.format(UserChoice, Rand))
        print('Computer wins.')
    else:
        print('You: {}\nComputer: {}'.format(UserChoice, Rand))
        print('YOU WIN')
        
else:
    print('Invalid option.\n')

print('-='*10)