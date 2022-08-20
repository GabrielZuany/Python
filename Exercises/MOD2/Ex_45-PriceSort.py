#Create a program that has a single tuple with the product names and their respective prices. At the end, show a list of prices organized in a tabular way

item = ('item 1', 1.75, 'object 2', 2, 'thing 3', 3, 'trêm 4', 9.15, 'item 5', 4,
        'item 1', 6, 'object 2', 2.47, 'thing 3', 3.50, 'trêm 4', 9.15, 'item 5', 4)

print('_'*37)
print(f'\n{"PRODUCT LIST":^37}')
print('_'*37)

for count in range (0, len(item)):
    if count%2 == 0:
        print(f'{item[count]:.<30}', end='')#...... until length 30 (aligned by left)
    else:
        print(f'R${item[count]:>5.2f}')#.... until length 5 (aligned by right), 2 float points

print('_'*37)