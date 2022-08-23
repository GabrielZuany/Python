#Develop a program in witch 4 players roll a dice and got random results. Save the results in a dicitonary. At the end, sort that dictionary and show the winner (the one who got the higher number).
from random import randint
from time import sleep
from operator import itemgetter

players = dict()
'''players = {'player1': randint(1, 6),
           'player2': randint(1, 6),
           'player3': randint(1, 6),
           'player4': randint(1, 6),}'''
ranking = list()

for count in range(1, 6):#read playerN: dice
    players[f'player{count}'] = randint(1,6)

print('*'*15, 'PLAYING','*'*15)
for keys, values in players.items():
    print(f'{keys} -> {values}')
    sleep(0.5)
print('*'*40)

ranking = sorted(players.items(), key = itemgetter(1), reverse=True)

print('*'*15, 'RANKING','*'*15)
for position, value in enumerate(ranking):
    print(f'{position+1} position = {value[0]} -> {value[1]}')
    sleep(0.5)
print('*'*40)

'''from random import randint
from time import sleep
from operator import itemgetter

player_info = dict()
game_data = list()

for count in range(0, 4):
    player_info['name'] = (f'Player{count+1}')
    player_info['dice'] = randint(1, 6)
    game_data.append(player_info.copy())

print('*'*15, 'PLAYING','*'*15)

for count in range(0, 4):
    print(game_data[count].values())
    sleep(0.5)
    
print('*'*40)'''