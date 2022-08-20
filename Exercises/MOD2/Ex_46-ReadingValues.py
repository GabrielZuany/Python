#Make a program that reads 5 values ​​and stores them in a list. At the end, show the highest and lowest value entered, and their respective positions.
values = list() #Orvalues = []

for count in range (0, 5):
    values.append(int(input('Insert a number to store: ')))

for ind in range (0, 5):
    if values[ind] == max(values):
        high = ind
    elif values[ind] == min(values):
        low = ind

print(f'You list is {values}')
print(f'The highest value is {max(values)} in position {high+1}')
print(f'The lowest value is {min(values)} in position {low+1}')