#Build a script that generates a random number between 0 and 10. Then, challenge the user to guess that number. Print the attempts needed by user to guess the number.
from random import randint
rand = randint(0,10)
UserNum = 11
attempt = -1

while UserNum != rand:
    UserNum = int(input('Try to guess the number (0-10): '))
    attempt+=1
    if UserNum < rand:
        print('Low value...', end = '')
    elif UserNum > rand:
        print('High value...', end = '')
    print('Attempts: {}' .format(attempt+1))
    
print('\n')
print('-='*10)
print('WINNER!\nNumber: {}\nAttempts: {}' .format(rand, attempt+1))
print('-='*10)