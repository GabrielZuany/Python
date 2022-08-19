#Make a even and odd game. You will play with computer and at the end, the program must show how many times you won.
from random import randint

flag = 'Y'
UserPoints = 0
CompPoints = 0

while flag != 'N':
    CompNum = randint(0,10)

    UserNumber = int(input('\nInsert a number between 0 and 10: '))

    if  0 < UserNumber > 10:
        print('Please, insert a valid value!')
        continue

    UserChoice = str(input('Even or odd? [E/O]')).upper()

    if UserChoice not in 'EO':
        print('Please, insert a valid option!')
        continue

    if (UserNumber + CompNum)%2 == 0:
        if UserChoice == 'E':
            print(f'\nThe sum is {UserNumber+CompNum}, and it is EVEN!\nYou win!!')
            UserPoints+=1
            continue
        else: CompPoints+=1

    else:
        if UserChoice == 'O':
            print(f'The sum is {UserNumber+CompNum}, and it is ODD!\nYou win!!')
            UserPoints+=1
            continue
        else: CompPoints+=1
            
    print('\nYou lost!!')
    print('-'*15)
    print('GAME OVER!\nYou {} x Comp {}' .format(UserPoints, CompPoints))
    print('-'*15)
    flag = str(input('Do you want to play again? [Y/N]')).upper()

print('Program finished...')