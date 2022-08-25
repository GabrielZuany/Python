#Make a script to generate 5 random numbers to put them in a tuple. Show the list and the higher and lower numbers.
from random import randint

Tuple = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('Tuple {} ' .format(Tuple))
print('Sorted tuple {}' .format(sorted(Tuple)))
print(f'Higer: {max(Tuple)}\nLower: {min(Tuple)}')

'''Higher = -1
Lower = 11
for count in range (0, 5):
    if Tuple[count] > Higher:
        Higher = Tuple[count]
    elif Tuple[count] < Lower:
        Lower = Tuple[count]

print(f'Higer: {Higher}\nLower: {Lower}')'''