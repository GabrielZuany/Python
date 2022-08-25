#Make a program that helps a mega sena player to create guesses. The program will ask how many games will be generated and will randomly select 6 numbers between 1 and 60 for each game, registering them in a composite list.
from random import randint

NumberOfGames = int(input('Number of games: '))
temp = list()
guess = list()
count = 0

for games in range(0, NumberOfGames):
    while True:
        value = randint(0,60)
        if value not in temp:
            temp.append(value)
            count+=1
        if count>=6:
            count = 0
            break
        
    temp.sort()
    guess.append(temp[:])
    temp.clear()

print('\n', '-'*10, 'GUESSES', '-'*10)
for pos, guesses in enumerate(guess):
    print(f'Game {pos+1} -> {guesses}')
print()