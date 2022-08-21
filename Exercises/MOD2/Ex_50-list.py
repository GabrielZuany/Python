#Built a script to read 7 values came by standard input and insert them on a list. Keep them separated by odd or even (main list with 2 list inside). At the end show the even and odd values sorted.
group = [[], []]

for count in range(0, 7):
    value = int(input('-> '))
    if value%2==0:
        group[0].append(value)
    else:
        group[1].append(value)
print(f'Even -> {group[0]}')
print(f'Odd -> {group[1]}')


#ANOTHER RESOLUTION
'''
odd = list()
even = list()
group = list()

for count in range(0, 7):
    group.append(int(input('Integer -> ')))
    
for value in group:
    if value%2 == 0:
        even.append(value)
    else:
        odd.append(value)
print(f'Even -> {even}')
print(f'Odd -> {odd}')
'''