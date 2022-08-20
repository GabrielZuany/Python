'''Make a script the reads a undertemined number of values (while user want to). If the current typed value already is on the list, do not add that value. At the end:
A)print the list sorted and the quantity numbers inserted.
B)Build two more lists -> 1.Only with even numbers; 2.Only with odd numbers.'''

values = list()
odd = list()
even = list()
choice = 'Y'
count = 0

while choice == 'Y':
    item = int(input('Insert a number: '))
    
    if item not in values:
        print(f'{item} add to list...')
        values.append(item) 
    else:
        print(f'{item} already on the list!')
    count+=1
    choice = str(input('Do you want to keep inserting values? [Y/N] ')).upper()
        
for i in range (0, len(values)):
    if values[i]%2 == 0:
        even.append(values[i])
    else:
        odd.append(values[i])

print(f'''\nYour list is {sorted(values)}\nYou have inserted {count} values. {len(values)} was valid.\nEven values: {even}\nOdd values: {odd}''')